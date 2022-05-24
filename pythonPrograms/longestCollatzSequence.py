#    2022-05-23
#    largestProductInAGrid.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 14 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 largestProductInAGrid.py

#



def collatz(n):
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
        elif n % 2 == 1:
            n = 3*n + 1
        counter += 1
    counter += 1
    return counter

max = 0
file = open("data.dat", "w")
for i in range(1,1000000):
    c = collatz(i)
    if c > max:
        max = c
    file.write(str(i) + "\t" + str(c) + "\n")

print(max)
file.close()
