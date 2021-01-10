# @Author: Diego Sarceno
# 12.08.2020
# Update:

# Problem 22 of Project Euler

'''Este programa toma el archivo de nombres, se rodenan alfabeticamente y se
calcula el score de dicha palabra. Es decir, suma cada una de las posiciones
de las letras que lo conforman y lo multiplica por su posicion en la lista
ordenada alfabeticamente.'''

# se abre el archivo
f = open('p022_names.txt','r')

# se agregan a una lista y se ordenan alfabeticamente
nombres = sorted([i[1:len(i) - 1] for i in f.readline().split(",")])

# Diccionario de letras a su posicion en el alfabeto
letras_posicion = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8,\
 "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16 , "Q":17, \
"R":18, "S":19 , "T":20, "U":21, "V":22, "W": 23, "X":24, "Y":25, "Z": 26}

def palabra_a_valor(palabra):
    suma = 0
    for letra in palabra:
        suma += letras_posicion[letra]
    return suma

total = 0
for i,nombre in enumerate(nombres):
    total += palabra_a_valor(nombre) * (i + 1)

print(total)
