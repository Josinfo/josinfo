#!/usr/bin/python3

# Exemplo LoopInfinito
aux = True
x = 1 

while aux == True:
    print("Executando: {}".format(x))
    x += 1
    if x == 11:
        aux = False
        
print("O While POWER acabou !")
