# @Author: Diego Sarceno
# 28.06.2020
# Update: 3.08.2020


import math as m

'''Archivo con funcines utiles'''

# 1. Funcion que determina si un numero es primo o no
def prime(n):
    '''La funcion toma como valor un numero y si este es primo, lo devuelve,
    sino no devuelve nada'''
    # para obviar el numero 1
    if (n <= 1):
        return(None)

    for i in range(2,m.ceil(m.sqrt(n)) + 1):
        if (n % i == 0) and (i != n):
            return(None)
    return(n)


def n_triang(n):
    '''Esta funcion toma un numero y encuentra su numero triangular asociado,
    i.e. n = 1 -> 1
    n = 2 -> 3
    asi sucesivamente'''
    return n*(n + 1)/2


def digSum(n):
    '''se convierte al numero en un str y se iteran sus digitos sumandolos'''
    suma = 0
    for i in range(len(str(n))):
        suma += int(str(n)[i])
    return suma
