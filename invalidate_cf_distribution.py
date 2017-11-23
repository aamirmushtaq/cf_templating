from urllib.request import urlopen
import argparse
import sys
import boto3
import json
import time


def load_json(args):
    try:
        json_file = urlopen(args.JSONPATH)
        json_obj = json.load(json_file)
        return json_obj
    except Exception as E:
        print("Error Converting to JSON. Exception is " + E)

def invalidate_distributions(json_obj):
    try:
        for item in json_obj['cloudfront']:
            if item.__contains__('tags'):
                if item['tags'].__contains__('reset'):
                    DistributionID=item['id']
                    try:
                        # I have used the credential within this code since I dont know how the executor has setup their dev environment.
                        # Please add the values here or if boto is properly configured, Proceed with the other option
                        cf = boto3.client('cloudfront', aws_access_key_id='ABCDEFGHIJKLMNOP',
                                            aws_secret_access_key='QRSTUVWXYZABCDEFGHIJKLMMN')
                        # In case Boto and aws credentials are properly configured on executing system, you can use below to proceed.
                        #cf = boto3.client('cloudfront')
                        invalidation = cf.create_invalidation(DistributionId=DistributionID,
                                                              InvalidationBatch={'Paths': {'Quantity': 1, 'Items': ['/*']},
                                                                                 'CallerReference': str(time.time())})
                        if invalidation['ResponseMetadata']['HTTPStatusCode'] == 201:
                            print("The invalidation for DistributionID " + DistributionID + " Is Created")
                    except Exception as E:
                        print("Error Creating Invalidation for Distribution ID: " + DistributionID +". Check if Distribution ID is valid or aws credentials are properly set")

    except Exception as E:
        print("Error in Distribution invalidation" + E)

def main():
    parser = argparse.ArgumentParser(description='Cloudfront JSON processing')
    parser.add_argument('JSONPATH')
    if len(sys.argv) < 2:
        print("Please provide url of JSON to process to this script")
    try:
        args = parser.parse_args()
    except Exception as E:
        print("Error Loading Value into arg parser\n" + E)
    json_obj = load_json(args)
    invalidate_distributions(json_obj)

if __name__ == '__main__':
    main()

