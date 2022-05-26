#    2022-05-24
#    amicableNumbers.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 21 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 amicableNumbers.py

import math as m

# suma total
sum = 0

def d(n):
    factorSum = 0
    for i in range(1,m.ceil(n/2) + 1):
        if n % i == 0 & n != i:
            factorSum += i
    return factorSum


sums = [(i,d(i)) for i in range(1,10000)]

for i in range(len(sums)):
    for j in range(i,len(sums)):
        if sums[i][1] == sums[j][1] & sums[i][0] != sums[j][0]:
            sum += sums[i][1] + sums[j][1]


'''
for i in range(1,10000):
    for j in range(1,10000):
        if d(i) == j & d(j) == i & i != j:
            sum += j + i
'''
print(sum/2)
