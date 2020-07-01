x = 0
count = 1
while count <=1000:
    if (count % 3 == 0) or (count % 5 == 0):
        x = x + count
    else:
        None
    count = count +1

print(x)