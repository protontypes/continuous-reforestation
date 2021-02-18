#!/usr/bin/python3
import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    RAAS_API_KEY = os.environ['RAAS_API_KEY']

    my_output = f"Hello {RAAS_API_KEY}"

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
