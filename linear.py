from numpy import random

arr=random.randint(66,100,19)
min=arr[0]

for i in arr:
    if i<min:
        min=i
print(min)

