#    2022-05-23
#    largestProductInAGrid.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 11 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 largestProductInAGrid.py

'''
Tomando los datos del grid de 20x20 dado, se toman todos los grupos de 4 adyacentes (arriba, abajo, lados y diagonales) y encontrar el producto más grande.
'''


# lectura del archivo
file = open('largestProductInAGrid.txt','r')
data = [line.split() for line in file]
file.close()

for i in range(len(data)):
    for j in range(len(data[0])):
        data[i][j] = int(data[i][j])

max = 0
for line in data:
    for i in range(len(line) - 3):
        step = line[i]*line[i + 1]*line[i + 2]*line[i + 3]
        if step > max:
            max = step


for i in range(len(data) - 3):
    for j in range(len(data[0])):
        step = data[i][j]*data[i + 1][j]*data[i + 2][j]*data[i + 3][j]
        if step > max:
            max = step

for i in range(len(data) - 3):
    for j in range(len(data[0]) - 3):
        step = data[i][j]*data[i + 1][j + 1]*data[i + 2][j + 2]*data[i + 3][j + 3]
        if step > max:
            max = step

data = data[::-1]

for i in range(len(data) - 3):
    for j in range(len(data[0]) - 3):
        step = data[i][j]*data[i + 1][j + 1]*data[i + 2][j + 2]*data[i + 3][j + 3]
        if step > max:
            max = step
print("\n")
print(max)





















# END PROGRAM
