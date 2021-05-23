#!/usr/bin/python3
__author__ = 'Josinfo'

import requests
from requests.auth import HTTPBasicAuth

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AUTH = HTTPBasicAuth('ccie','ccie')
MEDIA_TYPE = 'application/yang-data+json'
HEADERS = {'Accept':MEDIA_TYPE, 'Content-Type':MEDIA_TYPE}

def get_request(url):
    response = requests.get(url,auth=AUTH,headers=HEADERS,verify=False)
    print ("API:",url)
    print (response.status_code) 
    if response.status_code in [200,202,204]:
        print("Successful")
    else:
        print ("Error in API Request")
    print (response.text)
    print ("=" * 40)
    print ("=" * 40)


#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/interface"
#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/router/" 
#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/router/bgp=6511"
url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/router/bgp=6511/bgp/router-id"
#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/router/ospf=1/router-id"
# 
get_request(url)