#    2022-05-23
#    latticePaths.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 14 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 latticePaths.py

'''
    cada vértice de la latice, el número de caminos posibles está dado por la
    combinación mCk, donde n = coordenada x y k es la coordenada -y-, con
    m = n + k. Con el origen en una de las esqunas del grid.
'''

import math as m

n = 20
k = 20

paths = m.factorial(n + k)/(m.factorial(n)*m.factorial(k))
print(paths)
