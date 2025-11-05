import requests as r
import time as t
from datetime import datetime as dt

url = 'https://api.tfl.gov.uk/BikePoint'

response = r.get(url,timeout=10)

print(response.status_code)
