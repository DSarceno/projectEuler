#    2022-05-26
#    circularPrimes.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 21 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 circularPrimes.py

import itertools
import functions as fun

def circle(num):
    part = ''
    tperm = list(itertools.permutations(str(num),len(str(num))))
    perm = []
    for t in tperm:
        for l in t:
            part += l
        perm.append(part)
        part = ''
    return perm

primes = []
for i in range(2,1000001):
    if fun.prime(i) == i:
        primes.append(i)

counter = 0
for p in primes:
    for circ in circle(p):
        if fun.prime(int(circ)) == int(circ) & counter == len(circle(p)):
            counter += 1
