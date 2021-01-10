# @Author: Diego Sarceno
# 9.8.2020
# Update:

# Problem 67 of Project Euler

'''De la piramide de numeros se dividirá en listas, para generar la mayor
suma se lee la piramide de abajo hacia arriba para asegurar la mayor suma
posible. El numero se importará de un archivo de texto'''

DATA = open('maximumPathSum2DATA.txt','r')

lines = DATA.readlines()

# para dividir en listas y volver enteros todos sus datos
for i in range(len(lines)):
    lines[i] = lines[i].strip().split(' ')
    lines[i] = [int(x) for x in lines[i]]


for i in range(len(lines)-2,-1,-1):
    for j in range(len(lines[i])):
        lines[i][j] = lines[i][j] + max(lines[i+1][j], lines[i+1][j+1])
    lines.pop()


print(lines[0][0])
