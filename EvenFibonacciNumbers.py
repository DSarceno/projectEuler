# @Author: Diego Sarceno
# 2019

# Problem 2 of Project Euler


x = []

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        x.append(a)
        a, b = b, a+b
    print()

m = input('Ingrese el número máximo para la suseción: ')
fib(int(m))
print(x)

myList = []

for y in x:
    if y % 2 == 0:
        myList.append(y)
    else:
        None

print(myList)
