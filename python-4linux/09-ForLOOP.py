#!/usr/bin/python3

"""
Criar um programa que print os numero .
"""

__author__ = 'Josinfo'
num = int(input("Descubra Raiz Quadrada: "))
listrange = list(range(1,num+1))

divisorlist = []
for number in listrange:
    if num % number == 0:
        divisorlist.append(number)
print(divisorlist)
