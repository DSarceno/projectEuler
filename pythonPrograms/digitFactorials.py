#    2022-05-26
#    digitFactorials.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 21 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 digitFactorials.py

import subprocess
import math as m

limit = 10000000
sum = 0

file = open('data2.dat','w')

for i in range(3,limit):
    partial = 0
    for x in str(i):
        partial += m.factorial(int(x))
    if i == partial:
        sum += i
        print(i)
        file.write(str(i) + '\t' + str(partial) + '\n')
file.close()
print(sum)

subprocess.call(['gnuplot','digitFactorials.gp'])
