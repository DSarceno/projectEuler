# @Author: Diego Sarceno
# 2019

# Problem 2 of Project Euler


x = []
#  se crea la funcion que encuentre los numeros de fibonacci
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        x.append(a)
        a, b = b, a+b
    return()

m = 4000000
fib(int(m))
print(x)

# se tomman unicamente los numeros pares


for y in x:
    if y % 2 != 0:
        x.remove(y)
    else:
        None

print(x)

# se toman los elementos de la lista y se suman
sum = 0
for i in x:
    sum += i

print(sum)
