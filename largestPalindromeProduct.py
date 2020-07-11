# @Author: Diego Sarceno
# 11.07.2020

'''
Programa que encuentra el numero palindromico
mas grande generado por dos numeros de 3 digitos
'''

# Se define una funcion que determina si es un numero palindromico
def nPal(n):
	return(str(n) == str(n)[::-1])

# se toman los numeros del 100 al 999 y se multiplican
p = 0
list_pal = []
for i in range(100,1000):
	for j in range(100,1000):
		p = i*j
		if nPal(n = p) == True:
			list_pal.append(p)

# se encuentra el m�aximo de la lista
large_palindromic = max(list_pal)
print(large_palindromic)
