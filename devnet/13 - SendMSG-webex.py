import requests
import json

url = "https://webexapis.com/v1/messages"

payload = json.dumps({
  #Sala Instrutores DevNet
  #"roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOGIxYzdmZDAtYjJhOS0xMWViLTkyMGMtYmI1Mzg2OTE2Yzlk",
  #
  #Sala Ozumaru
  "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vMDkyZDY5ZTAtYmMwZC0xMWViLWFlZTYtYzEzYTdkNTY3MmY4",
  
  "text": "Greetings from JosinfoXtreme - by Python"
})
headers = {
  'Authorization': 'Bearer ZDYyZjk5ZmQtNmE2OC00MDllLThjZTAtYWI3MDFhNmQ0NDVmMjFkY2I1MTItM2Fh_PF84_consumer',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)