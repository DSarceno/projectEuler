# @Author: Diego Sarceno
# 9.8.2020
# Update:

# Problem 13 of Project Euler

'''Se importaran los numeros de un archivo se sumaran, y se tomara
el primer paquete de 10 digitos'''

# se abre el archivo de datos y se lee ('r')
DATA = open('largeSumDATA.txt','r')

num = [l.split() for l in DATA]

# se suman todos los numeros
suma = 0
for i in range(len(num)):
    suma += int(num[i][0])

# se imprimen sus 10 digitos como un numero entero
print(int(str(suma)[0:10]))
