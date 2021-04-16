#!/usr/bin/python3

# Exemplo Input

"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

name = input ("Qual seu Nome: ")
age = int(input("Qual sua idade: "))
year = int(input("Em que ano estamos: "))
time = str((year-age)+100)
print (name + "Seu aniversario de 100 anos será em:" + time)