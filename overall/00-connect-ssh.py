from netmiko import ConnectHandler

import getpass

user = (input("Digite seu usuario:? "))
pswd = getpass.getpass() 

#First create the device object using a dictionary
NXOS = {
    'device_type': 'cisco_nxos',
    'ip': '10.14.0.1',
    'username': user,
    'password': pswd
}
 
# Next establish the SSH connection
net_connect = ConnectHandler(**NXOS)
 
# Then send the command and print the output
output = net_connect.send_command('show ip int brief')
print (output)
 
# Finally close the connection
net_connect.disconnect()