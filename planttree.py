#!/usr/bin/python3
import os
import requests
from urllib.parse import urljoin
import posixpath
import json


def main():
    # Variables set by the CI script
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
    headers = {"x-api-key": api_key}

    # Check of we run in development or production mode
    # Using the sandbox API does not require any API key
    if production == "true":
        print("Using production API")
        url = "https://api.digitalhumani.com/tree"
    else:
        print("Using sandbox API for development")
        url = "https://api-dev.digitalhumani.com/tree"

    # run the RaaS request
    r = requests.post(url, json=body_para, headers=headers)

    # put the response int a dictionary
    response = json.loads(r.text)

    # create a simple human readable response message
    if r.status_code == requests.codes.ok:
        print(
            "Request successful\n"
            + str(response["user"])
            + " planted "
            + str(response["treeCount"])
            + " tree(s). "
            + "Find more information on dashboard: "
            + "https://digitalhumani.com/dashboard/"
            + str(enterprise_id)
            + ".html"
        )
    else:
        print("Something went wrong. \n Your error code is: " + str(r.status_code))
        os._exit(1)
    
    # return the dict to the CI script for following data processing
    print(f"::set-output name=response::{response}")


if __name__ == "__main__":
    main()
