# Testing to make sure the environment installed properly

# Imports

#Py-ART, simply the best sowftware around.. Give those guys a grant
import pyart

#Boto3 is the AWS SDK
import boto3

#plotting
import matplotlib

#plotting on a maop
import cartopy

if __name__ == "__main__":
    print("Imports have completed, this is good")
    print("Testing Py-ART Version")
    print(pyart.__version__)
    print("Testing boto3 version")
    print(boto3.__version__)
    print("Testing Matplotlib version")
    print(matplotlib.__version__)
    print("testing Cartopy version")
    print(cartopy.__version__)
    print("SUCCESS")