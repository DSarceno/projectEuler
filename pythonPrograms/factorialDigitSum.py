#    2022-05-2
#    factorialDigitSum.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 20 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 factorialDigitSum.py

import math as m

cien = m.factorial(100)

sum = 0
for digit in str(cien):
    sum += int(digit)

print(sum)
