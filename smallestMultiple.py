# @Author: Diego Sarceno
# 11.07.2020

# Problem 5 of Project Euler

'''
Tomamos cada numero hasta encontrar el minimo
divisible entre todos del 1 al 20
'''

import math as m

# esto porque el numero o es ese o es menor al producto de todos sus divisores
cota_i = 230000000

def div(n):
    for i in range(11,21):
        if (n % i != 0):
            return False
    return True

count = cota_i
while True:
    if div(count):
        break
    count += 2

print(count)
