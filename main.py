"""
Copyright (c) 2018 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Doron Chosnek"
__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"

# pylint: disable=invalid-name
 
import json
import argparse
import requests.packages.urllib3
from tetpyclient import RestClient
requests.packages.urllib3.disable_warnings()


# =============================================================================
# FUNCTIONS
# -----------------------------------------------------------------------------

def mini_api_explorer(client):
    resp = client.get('/openapi/v1/' + args.show)
    if resp.status_code == 200:
        print json.dumps(resp.json(), indent=2)
    else:
        print resp

def main():
    '''Insert your script logic here instead
    '''
    print "Hello, Tetration!"

# =============================================================================
# MAIN
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # -------------------------------------------------------------------------
    # ARGPARSE

    parser = argparse.ArgumentParser(description='Cool Tetration script.')
    parser.add_argument('--tetration', required=True, help="URL of Tetration instance")
    parser.add_argument('--credentials', default='api_credentials.json', help="path to credentials file")
    parser.add_argument('--show', help="miniature API explorer")
    args = parser.parse_args()

    restclient = RestClient(
        args.tetration,
        credentials_file=args.credentials,
        verify=False
    )
    requests.packages.urllib3.disable_warnings()

    # -------------------------------------------------------------------------
    # This logic will either run the mini-api-explorer once and exit or it will
    # run the main function and exit

    if args.show is not None:
        mini_api_explorer(restclient)
    
    else:
        main()
