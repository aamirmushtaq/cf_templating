# cf_templating
AWS CF operations using python and aws sdk
## Requirements:
  # Python 3.6 
  ### Steps for ubuntu 14 / 16:
    sudo add-apt-repository ppa:jonathonf/python-3.6
    sudo apt-get update
    sudo apt-get install python3.6
  # Boto3
  ### Steps for installing Boto3
    python3.6 -m pip install boto3
  # Adding AWS Credentials within source code
  I went the hard coded way due to lack of time and also since i was not sure if the dev environment would have boto installed and configured properly or not. 
  Please edit the python file with the correct aws keys and secret key and run it. 
  If boto is configured already, then uncomment the second option on line 29 and comment out the one at 26, 27
 
# Running the program:
The program expects a command line param which is the input json file based on which it will be doing the invalidations.
A sample Input file is already committed to this repo for example. 
execute the program like below :
    
    python3.6 invalidate_cf_distribution.py https://raw.githubusercontent.com/aamirmushtaq/cf_templating/master/input.json
  
Note: You can point it to any url and it should work. 
