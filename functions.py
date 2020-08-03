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
