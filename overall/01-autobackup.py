#/usr/bin/python3

# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler
import getpass
import sys
import time

with open('XPI_Devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'admin',
            'password': 'admin'
        }
 
 #** Função kwargs le o que contem no dicionario

        net_connect = ConnectHandler(**Router)
        hostname = net_connect.find_prompt().replace('#','')
        print ("Backup do " + hostname)
 
        filename = '/c/Users/u004768/Documents/NETWORK-OVERALL/04- DEVNET/GITHUB/josinfo/overall/' + hostname + '.txt'
      
        showrun = net_connect.send_command('show run')
       #showvlan = net_connect.send_command('show vlan')
       #showver = net_connect.send_command('show ver')
        log_file = open(filename, "a")   # in append mode
        log_file.write(showrun)
        log_file.write("\n")
        #log_file.write(showvlan)
        #log_file.write("\n")
        #log_file.write(showver)
        #log_file.write("\n")
        log_file.close()

# Finally close the connection
        net_connect.disconnect()