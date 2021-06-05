#!/usr/bin/python3
__author__ = 'Josinfo'

from netmiko import ConnectHandler
import getpass

user = (input("Digite seu Usuario:? "))
pswd = getpass.getpass() 
caixas = []

sn = 'yes'
c = 0
while sn == 'yes':
    c += 1
    caixas.append(input (f"Enter {c}° device IP: "))
    sn = input("Deseja um novo equipamento (yes/no): ")

while True:
    for i in caixas:
        print(i)
        LEGADO = {
            'device_type': 'cisco_nxos',
            'ip': i,
            'username': user,
            'password': pswd
            }
        net_connect = ConnectHandler(**LEGADO)  
        comandos = open("comandos.txt", "r").readlines()
        for cmd in comandos:
            with open(f"{i}.txt", "a") as file:
                file.write(cmd)
                file.write(net_connect.send_command(cmd))
                file.write("="*10)
        net_connect.disconnect()
    print ("="*20, "\n","\t","All done!","\n","="*20)
    break