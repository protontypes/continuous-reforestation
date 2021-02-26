#!/usr/bin/python3
import os
import requests
from urllib.parse import urljoin
import posixpath
import json


def main():
    # Variables set by the integration.yml script
    enterprise_id = os.environ["INPUT_ENTERPRISEID"]
    project_id = os.environ["INPUT_PROJECTID"]
    user = os.environ["INPUT_USER"]
    treecount = int(os.environ["INPUT_TREECOUNT"])
    production = os.environ["INPUT_PRODUCTION"]
    api_key = os.environ["INPUT_APIKEY"]

    # REST API Parameters 
    body_para = {
        "treeCount": treecount,
        "enterpriseId": enterprise_id,
        "projectId": project_id,
        "user": user,
    }

    # Using the sanbox API does not require any API key
    if production == "true":
        print("Using production API")
        url = "https://api.digitalhumani.com/tree"
    else:
        print("Using sandbox API for development")
        url = "https://api-dev.digitalhumani.com/tree"
    headers = {"x-api-key": api_key}
    # run the RaaS request
    r = requests.post(url, json=body_para, headers=headers)

    # put the response int a dictionary for easier handling later
    response = json.loads(r.text)

    # "later" handling
    message = ""
    if r.status_code == requests.codes.ok:
        message = (
            "Request successful\n"
            + str(response["user"])
            + " planted "
            + str(response["treeCount"])
            + " tree(s)."
        )
    else:
        message = "Something went wrong. \n Your error code is: " + str(r.status_code)

    print(f"::set-output name=response::{response}")


if __name__ == "__main__":
    main()
