#!/usr/bin/python3
import os
import requests  # noqa We are just importing this to prove the dependency installed correctly
from urllib.parse import urljoin
import posixpath


def main():
    RAAS_API_KEY = os.environ['RAAS_API_KEY']
    development_API = "https://api-dev.digitalhumani.com/"
    production_API = "https://api.digitalhumani.com/"
    enterprise_ID = "cd7cedcd"
    build_URL = posixpath.join(development_API,"enterprise",enterprise_ID)
    print(build_URL)
    r = requests.get(build_URL)
    my_output = f"{r}"

    print(f"::set-output name=myOutput::{r}")

if __name__ == "__main__":
    main()
