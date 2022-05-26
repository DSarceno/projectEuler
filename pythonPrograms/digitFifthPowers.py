#    2022-05-24
#    digitFifthpowers.py
#    Diego Sarceño (dsarceno68@gmail.com)

#    problem 21 project euler

#    Codificación del texto: UTF8
#    Compiladores probados: Python (Ubuntu 20.04 Linux) 3.8.5
#    Instrucciones de importación: requiere módulo regex.
#    python3 digitFifthpowers.py

sol = 0
for i in range(2,5*9**5 + 1):
    if sum([int(x)**5 for x in str(i)]) == i:
        sol += i

print(sol)
