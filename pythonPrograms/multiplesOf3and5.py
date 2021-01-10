# @Author: Diego Sarceno
# 2019

# Problem 1 of Project Euler

x = 0

for i in range(3,1000):
	if (i % 3 == 0) or (i % 5 == 0):
		x += i

print(x)
