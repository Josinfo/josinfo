#!usr/bin/phython

#Operadores de Estrutura e decisão
idade = int (input("\n Qual sua idade: "))
cnh = input("\n Voçê possui CNH SIM/NAO: ")

if cnh.lower().strip() == "sim":
    cnh = True
if idade >= 18 and cnh == True:
    print("\n Tu já é Adulto e pode dirigir")
elif idade >= 18 and cnh != False:
     print("\n Va tirar a CNH Vagabundo")
else:
    print("\n Tu é uma criança va andar de busão")

#Operadores de Estrutura e decisão
