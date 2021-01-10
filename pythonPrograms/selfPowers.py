# @Author: Diego Sarceno
# 20.08.2020
# Update:

# Problem 48 of Project Euler

'''Este programa encuentra los ultimos 10 digitos de la suma 1-1000 cada
uno elevado a si mismo'''

suma = 0
for i in range(1,1001):
    suma += i**i
suma = str(suma)
print(int(suma[len(suma) - 10:len(suma)]))
