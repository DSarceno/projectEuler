# @Author: Diego Sarceno
# 28.06.2020

# Problem 3 of Project Euler

#x = 600851475143

# 1. se toma el numero y se encuentran sus factores primos
x = int(input('Ingrese el numero: '))
lista_divisores = []
for i in range(2,x):
    if x % i == 0:
        lista_divisores.append(i)
    else:
        None



print(lista_divisores)
for i in range(2,x):
    for j in lista_divisores:
        if (j % i == 0) and (j != i):
            lista_divisores.remove(j)
        else:
            None
print(lista_divisores)

Large_prime = max(lista_divisores)
print(Large_prime)
