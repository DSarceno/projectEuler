#    2022-05-23
#    numberLettersCounts.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 14 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 numberLettersCounts.py

from num2words import num2words
# cuantas letras tiene cada numero
characters = " -"
long = 0
for i in range(1,1000):
    num = num2words(i)
    for x in range(len(characters)):
        num = num.replace(characters[x],"")
    long += len(num)

print(long)
