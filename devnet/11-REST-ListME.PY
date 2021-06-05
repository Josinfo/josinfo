#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from __future__ import print_function
from webexteamssdk import WebexTeamsAPI


DEMO_ROOM_NAME = "webexteamssdk Demo Room"
DEMO_PEOPLE = ["jcaitano@gmail.com"]
DEMO_MESSAGE = u"Webex Teams rocks!"
DEMO_FILE_URL = \
    "https://www.webex.com/content/dam/wbx/us/images/dg-integ/teams_icon.png"
import requests

url = "https://webexapis.com/v1/people/me"

payload={}
headers = {
  'Authorization': 'Bearer ZDYyZjk5ZmQtNmE2OC00MDllLThjZTAtYWI3MDFhNmQ0NDVmMjFkY2I1MTItM2Fh_PF84_consumer'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)