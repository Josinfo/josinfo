#!/usr/bin/python3

file=open("cisco.txt","r")
for item in file:
    item=item.strip()
    print (item)
file.close()

equipamento=[]
file=open("cisco.txt","r")
for item in file:
    item=item.strip()
    equipamento.append(item)
file.close()

print(equipamento)