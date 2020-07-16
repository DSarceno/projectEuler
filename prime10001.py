# @Author: Diego Sarceno
# 13.07.2020

# Problem 7 of Project Euler

'''
Se encuentran los numeros primos con el algoritmo de eratostenes,
se almacenaran en una lista hasta que el numero de la lista sea
de 10001
'''

from math import *
count = 1
k = 1
Lista_n = [k + i for i in range(1,1000000)]

while len(Lista_n) <= 10001:
    for i in Lista_n:
        for j in Lista_n:
            if (j % i == 0) and (j != i):
                Lista_n.remove(j)
            else:
                continue
    count += 1

# se imprime el 10001 numero primo
print(Lista_n[10000])
