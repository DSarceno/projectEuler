# @Author: Diego Sarceno
# 2019

# Problem 2 of Project Euler

'''este problema toma una funcion que agrega los numeros de fibonacci
a una lista y se suman solo los numeros pares'''

import functions as fun

even = 0
for i in fun.fib(4000000):
    if (i % 2 == 0):
        even += i

print(even)
