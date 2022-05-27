#    2022-05-27
#    dBasePalindromes.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 36 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: nada
#    python3 dBasePalindromes.py

sum = 0
for num in range(1,1000000,2):
    if (str(num) == str(num)[::-1]):
        if (bin(num)[2:] == bin(num)[2:][::-1]):
            sum += num
            print(num, bin(num)[2:])

print(num)




















##
