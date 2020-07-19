# @Author: Diego Sarceno
# 13.07.2020

# Problem 7 of Project Euler

'''
Se encuentran los numeros primos con el algoritmo de eratostenes,
se almacenaran en una lista hasta que el numero de la lista sea
de 10001
'''

# se toma un contador iniciando en 2
count = 2

for i in range(1,200000,2): # paso 2 para evitar todos los numeros pares
    k = 1
    while k < i:
        k += 2
        if (i % k == 0):
            break
        if (k + 2 == i):
            count += 1
        if count == 10001:
            print(i)
