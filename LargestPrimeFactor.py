#x = 600851475143
x = 20
myList = []
myList2 = []
count = 1

while count <= x:
    if x % count == 0:
        myList.append(count)
    else:
        None
    count = count + 1

print(myList)

for y in myList:
    for num in range(1,y):
        if num % y != 0:
            myList2.append(y)
        else:
            None

print(myList2)
