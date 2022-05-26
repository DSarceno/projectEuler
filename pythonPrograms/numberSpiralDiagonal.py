#    2022-05-24
#    numberSpiralDiagonal.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 21 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 numberSpiralDiagonal.py


## impares
odd = range(1,1001*1001 + 1,2)

dim = 1001*1001
sum = 1
count = 1
i = 0

while odd[i] != dim:
    for j in range(4):
        i += count
        sum += odd[i]
    count += 1

print(sum)
