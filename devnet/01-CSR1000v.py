from getpass import getpass
from netmiko import ConnectHandler

device = {
    'device_type':'cisco_ios',
    'host':'ios-xe-mgmt.cisco.com',
    'port':8181,
    'username':'developer',
    #'password':getpass()
    'password':'C1sco12345'
}

with ConnectHandler(**device) as net_connect:
    #output = net_connect.send_command('show ip interface brief', use_textfsm=True)
    output = net_connect.send_command('show ip interface brief', use_genie=True)
    #output = net_connect.send_command('show ip interface brief')
print()
print(output)
#print(output[0]["ipaddr"])
print()
