from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "ios-xe-mgmt.cisco.com",
    "port": 8181,
    "username": "developer",
    #"password": getpass()
    "password":"C1sco12345"
}

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command("show ip interface brief", use_genie=True)

print()
pprint(output)
print()