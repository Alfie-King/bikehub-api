print('packages imported')
import requests as r
import time as t
from datetime import datetime as dt
import json 
import os
import boto3
import sys
from dotenv import load_dotenv 

from extract_bikepoint import extract
from load import load
print('loading functions')

url = 'https://api.tfl.gov.uk/BikePoint'

print('running extract')
extract(url)
print('extract done')

print('running load')
load()
print('load done')

print('script finished')