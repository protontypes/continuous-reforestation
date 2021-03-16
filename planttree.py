#!/usr/bin/python3
import os
import requests
from urllib.parse import urljoin
import posixpath
import json
import sys
import re


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
        url_numtrees = (
            "https://api.digitalhumani.com/enterprise/"
            + enterprise_id
            + "/treeCount?startDate=2010-03-01&endDate=2030-01-01"
        )

    else:
        print("Using sandbox API for development")
        url = "https://api-dev.digitalhumani.com/tree"
        url_numtrees = (
            "https://api-dev.digitalhumani.com/enterprise/"
            + enterprise_id
            + "/treeCount?startDate=2010-03-01&endDate=2030-01-01"
        )

    # run the RaaS requests for planting trees and getting tree count
    r = requests.post(url, json=body_para, headers=headers)
    r_numtrees = requests.get(url_numtrees, headers=headers)

    # put the response into a dictionary
    response = json.loads(r.text)
    response_alltrees = json.loads(r_numtrees.text)
    response_alltrees = str(response_alltrees)
    num_alltrees = re.findall("[0-9]+", response_alltrees)
    plantedTrees = num_alltrees[0]

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
            + ".html\n"
            + plantedTrees
            + " were now planted in total."
        )
    else:
        print("Something went wrong. \n Your error code is: " + str(r.status_code))
        sys.exit(1)

    # return the dict to the CI script for following data processing
    print(f"::set-output name=response::{response}")
    print(f"::set-output name=response::{plantedTrees}")


if __name__ == "__main__":
    main()
