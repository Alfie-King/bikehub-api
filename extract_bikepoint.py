import requests as r
import time as t
from datetime import datetime as dt
import json 

url = 'https://api.tfl.gov.uk/BikePoint'

def extract(url):
    
    response = r.get(url,timeout=10)
    retry_codes = [429,500,502,503,504] # All codes that we are wanting to retry
    print(f'attempting {url}')

    count = 0
    max_tries = 3

    while count < max_tries:
        # Tests if connection to API is successful
        if response.status_code == 200:
            print('successful call')
            # Tests if the API data type is JSON if yes runs code if no breaks and prints error message
            try:
                data = response.json()
            except Exception as e:
                print(e)
                break
            
            # Adds extract timestamp to file name to prevent overwriting
            extract_timestamp = dt.now() 
            for bp in data:
                bp['extract_timestamp'] = str(extract_timestamp)

            # Puts JSON in data folder in repo
            filepath = 'data/' + extract_timestamp.strftime('%Y-%m-%dT%H-%M-%S') + '.json'
            with open(filepath,'w') as file:
                json.dump(data,file)
            
            break 

        # If status code is one that should be retried the connection gets retried after 20 seconds
        elif response.status_code in retry_codes:
            print(response.reason())
            t.sleep(20)
            count += 1
        
        # If status code is any other, breaks while loop and out puts reason
        else:
            print(response.reason())
            count = 3
            break

    # Prints whether connection was successful or not        
    if count == max_tries:
        print('Connection failed')
    else:
        print('Connection successful')