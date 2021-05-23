import requests
import json

url = "https://webexapis.com/v1/rooms"

payload={}
headers = {
  'Authorization': 'Bearer ZDYyZjk5ZmQtNmE2OC00MDllLThjZTAtYWI3MDFhNmQ0NDVmMjFkY2I1MTItM2Fh_PF84_consumer',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
