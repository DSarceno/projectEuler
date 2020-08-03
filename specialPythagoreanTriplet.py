# @Author: Diego Sarceno
# 22.07.2020

# Problem 9 of Project Euler

'''
Se toman numeros entre 1 y 1000 y se encuentran aquellos que cumplan
las condiciones.
'''

# utilizamos ciclos para comprobar las hipotesis

for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if (a + b + c == 1000) and (a**2 + b**2 == c**2):
                print(a * b * c)
