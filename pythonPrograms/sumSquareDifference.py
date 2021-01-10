# @Author: Diego Sarceno
# 13.07.2020

# Problem 6 of Project Euler

'''
Se encuentra la diferencia entre la suma de los cuadrados de los
primeros 100 numeros y el cuadrado de la suma de los primeros 100 numeros
'''

# encontramos la suma de los primeros 100 numeros
sum_100 = 0
for i in range(1,101):
    sum_100 += i

# encontramos la suma de los cuadrados de los primeros 100 numeros naturales

sum_squared = 0
for i in range(1,101):
    sum_squared += i**2

# se imprime la diferencia

diff = sum_100**2 - sum_squared
print(diff)
