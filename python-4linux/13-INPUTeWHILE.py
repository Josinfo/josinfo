#!/usr/bin/python3
__author__ = 'Josinfo'

file = open("cisco.txt", "a")
while True:
    sn = input("Deseja um novo equipamento (yes/no): ")
    if sn == "yes":
        newItem = input("Enter device name: ")
        file.write(newItem + "\n")
    else:    
        print("="*20, "\n","\t","All done!","\n","="*20)
        break
file.close()


"""
Quantos Equipamento:2

Criar Lista de IP:
>> IP DEVICE01
>> IP DEVICE02

Quantos comandos:3
>> show 01
>> show 02
>> sho2 03

Acessar equipamento 
aplicar os comandos
Salvar .txt externo separando pelo IP

ALL DONE
"""
