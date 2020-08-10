# @Author: Diego Sarceno
# 7.8.2020
# Update:

# Problem 18 of Project Euler

'''De la piramide de numeros se dividirá en listas, para generar la mayor
suma se toma el primer numero luego, de los dos que tiene debajo, se toma
el mayor, y asi sucesivamente. El numero se importará de un archivo de texto'''

DATA = open('maximunPathSumDATA.txt','r')

lines = [l.split() for l in DATA]

lista = []
a = 0
for i in range(len(lines)):
    if len(lines[i]) == 1:
        first = int(lines[0][0])
        print(first)
        lista.append(first)
    else:
        m = max([int(lines[i][a]),int(lines[i][a + 1])])
        print(m)
        lista.append(m)
        if int(lines[i][a+1]) == m:
            a += 1

print(lista)
suma = 0
for i in lista:
    suma += i

print(suma)
