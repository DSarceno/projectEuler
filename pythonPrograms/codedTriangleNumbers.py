# @Author: Diego Sarceno
# 13.08.2020
# Update:

# Problem 42 of Project Euler

'''este programa toma cada letra de la palabra y determina si la suma
de los valores de cada letra forma un numero triangular y se cuentan cuantas
palabras triangulares hay en el documento'''

f = open("p042_words.txt", "r")

palabras = sorted([i[1:len(i) - 1] for i in f.readline().split(",")])

letras_a_numeros = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8,\
 "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, \
"R":18, "S":19, "T":20, "U":21, "V":22, "W": 23, "X":24, "Y":25, "Z": 26}

def palabra_a_valor(palabra):
    suma = 0
    for letra in palabra:
        suma += letras_a_numeros[letra]
    return suma

import functions as fun

conteo = 0
for palabra in palabras:
    if fun.TriangularQ(palabra_a_valor(palabra)):
        conteo += 1
print(conteo)
