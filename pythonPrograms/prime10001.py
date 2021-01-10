# @Author: Diego Sarceno
# 13.07.2020
# Update: 3.08.2020

# Problem 7 of Project Euler

'''Descripcion:
Se encuentran los numeros primos con el algoritmo de eratostenes,
el contador determina cuando se llega al primo 10001
'''

import functions as fun # del documento de funciones
import math as m

top = 105000
count = 1 # porque no se incluye el 2 en el conteo total

# se toma el numero y se valua para todos aquellos menores a el
for i in range(3,top,2):
    if (fun.prime(n = i) != None):
        count += 1
        if (count == 10001):
            print(i)
