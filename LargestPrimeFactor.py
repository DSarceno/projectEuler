# @Author: Diego Sarceno
# 28.06.2020
# Update: 3.08.2020

# Problem 3 of Project Euler

'''Descripcion:
Se define una funcion que determine si un numero es primo y se valuan los
divisores de dicho numero, estos divisores primos se comparan para
encontrar el mayor de ellos.
'''

import math as m
import functions as fun
# se toma el numero
x = 600851475143

# el algoritmo toma los multiplos de 'x' y los valua en la funcion
largest = 0
for i in range(3,round(m.sqrt(x))):
    if (x % i == 0):
        if (fun.prime(n = i) == None):
            None
        elif (largest <= prime(n = i)):
            largest = i

print(largest)
