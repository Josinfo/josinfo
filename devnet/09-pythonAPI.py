#!/usr/bin/python3
__author__ = 'Josinfo'


import requests
from requests.auth import HTTPBasicAuth

AUTH=HTTPBasicAuth('ccie','ccie')
MEDIA_TYPE='application/yang-data+json'
HEADERS={'Accept':MEDIA_TYPE,'Content-Type':MEDIA_TYPE}

def get_request(url):
    response = requests.get(url, auth=AUTH, headers=HEADERS, verify=False)
    print("API: ", url)
    print(response.status_code)
    if response.status_code in [200,202,204]:
        print("Successful")
    else:
        print("Error in API Request")
    print(response.text)
    print("=" * 40)
    print("=" * 40)

#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native"
#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/interface"
#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2"
url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/"
#url="https://192.168.15.157/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/address/"
#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/address/primary"
#url="https://192.168.15.172/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=2/ip/address/primary/address"

get_request(url)



