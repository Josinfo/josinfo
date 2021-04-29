#!/usr/bin/python3
__author__ = 'Josinfo'

from netmiko import ConnectHandler
import getpass

user = (input("Digite seu Usuario:? "))
pswd = getpass.getpass() 
caixas = []
#ip_address = open("Devices.txt","r")

#First create the device object using a dictionary
while True:
    sn = input("Deseja um novo equipamento (yes/no): ")
    if sn == "yes":
        caixas.append(input ("Enter device IP: ")) 
    else:    
        for i in caixas:
            print(i)
            LEGADO = {
            'device_type': 'cisco_nxos',
            'ip': i,
            'username': user,
            'password': pswd
            }
 
        #  Next establish the SSH connection
            net_connect = ConnectHandler(**LEGADO)  
            comandos = open("comandos.txt", "r").readlines()
            # Then send the command and print the output
                print(file)
            net_connect.disconnect()
        print("="*20, "\n","\t","All done!","\n","="*20)
        break
    

