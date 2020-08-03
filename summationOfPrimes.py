# @Author: Diego Sarceno
# 22.07.2020
# Update: 3.08.2020

# Problem 10 of Project Euler

'''Descipcion:
se utiliza la criba de Eratostenes para encontrar los numeros
primos menores a 2E6 y sumarlos
'''

import functions as fun
import math as m

top = 2000000
sum = 2 # para solo tomar impares en el rango

# se toma el numero y se valua para todos aquellos menores a el
for i in range(3,top,2):
    if (fun.prime(n = i) != None):
        sum += i

print(sum)
