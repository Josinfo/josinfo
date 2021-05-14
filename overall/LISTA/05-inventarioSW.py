#!/usr/bin/python3
author = 'Josinfo'


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
def count_lines01 (texto):
    lines = texto.count('Gi')
    return lines
def count_lines02 (texto):
    lines = texto.count('disabled')
    return lines
def count_lines03 (texto):
    lines = texto.count('notconnect')
    return lines
def count_lines04 (texto):
    lines = texto.count('connect')
    return lines

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
        comandos = open("interfaces.txt", "r").readlines()
        for cmd in comandos:
            with open(f"inventario.txt", "a") as file:
                # instancia.funcao(parametro)
                #file.write(cmd)
                comand_output = net_connect.send_command(cmd)
                #line_count01 = count_lines01(comand_output)
                line_count02 = count_lines02(comand_output)
                line_count03 = count_lines03(comand_output)
                #line_count04 = count_lines04(comand_output)
                file.write("\n"+"="*5 + " " + str(i) + "="*5 + "\n")
                #file.write("> Possui " + str(line_count01) + " Total de Portas \n") 
                file.write("> Possui " + str(line_count02) + " em modo Disabled \n")
                file.write("> Possui " + str(line_count03) + " em modo NotConnected \n")
                #file.write("> Possui " + str(line_count04) + " em modo Connected \n")

                #file.write(net_connect.send_command(cmd))
                file.write("\n"+"="*10)
        net_connect.disconnect()
    print ("="*20, "\n","\t","All done!","\n","="*20)
    break


