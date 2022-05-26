#    2022-05-24
#    thousandDigitFibNum.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 21 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 thousandDigitFibNum.py

import numpy as np

F = np.array([[1,1],[1,0]])
#print(np.linalg.matrix_power(F,3))

def fib(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
    return a

print(len(str(fib(10E500))))
'''
while len(str(F[0][1])) < 1000:
    F = np.dot(F,F)

print(F[0][1])
'''
