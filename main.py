#!/usr/bin/python3
import os
import requests  # noqa We are just importing this to prove the dependency installed correctly
from urllib.parse import urljoin
import posixpath
import json


def main():
    #RAAS_API_KEY = os.environ['RAAS_API_KEY']
    #my_output = f"{message}
    
    # header maybe
    # key: x-api-key
    # value: YOUR_API_KEY
    
    company_id = 'cd7cedcd'
    user = 'tjark'
    trees = os.environ['number_of_trees']
    body_para = {
            "treeCount": trees,
            "enterpriseId": company_id,
            "projectId": "93322249",
            "user": user
            }
    url = 'https://api-dev.digitalhumani.com/tree' # currently the dev API
    
    # run the post request
    r = requests.post(url, json=body_para)
    
    # put the response int a dictionary for easier handling later
    ddd = json.loads(r.text)
    
    # "later" handling
    message = ''
    if r.status_code == requests.codes.ok:
        message = 'Request went through. All good.\n'+str(ddd['user'])+' planted '+str(ddd['treeCount'])+' tree(s). Very nice.'
    else :
        message = 'Something went wrong. \n Your error code is: '+str(r.status_code)
    
    print(message)

    print(f"::set-output name=myOutput::{message}")

if __name__ == "__main__":
    main()
