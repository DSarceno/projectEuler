# @Author: Diego Sarceno
# 11.07.2020

# Problem 5 of Project Euler

'''
Tomamos cada numero hasta encontrar el minimo
divisible entre todos del 1 al 20
'''
# creamos una funcion
def div120(n):
    for i in range(3,21):
        if (n % i != 0):
            return False
    return True

# tomamos todos los numeros hasta encontrar el menor que cumpla
num = 20
while True:
    if div120(num):
        break
    num += 2

# El nuemro que pare el loop es el menor divisible entre 1 y 20
# se imprime
print(num)
