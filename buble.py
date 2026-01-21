from numpy import random

my_array = random.randint(1,15,10)

n=len(my_array)
print("random number between 1 to 15",my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]>= my_array[j+1]:
            my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
print("sorted numbers",my_array)