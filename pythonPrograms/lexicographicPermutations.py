#    2022-05-24
#    lexicographicPermutations.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 21 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 lexicographicPermutations.py

from itertools import permutations

def lexi(cadena):
    perm = sorted(''.join(chars) for chars in permutations(cadena))
    print(perm[999999])

cadena = '0123456789'
lexi(cadena)
