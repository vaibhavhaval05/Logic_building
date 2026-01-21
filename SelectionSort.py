a=[29, 10, 14, 37, 13]

for i in range(len(a)):
    minindex=i
    for j in range(i+1,len(a)):
        if a[j]<a[minindex]:
            minindex=j
    a[i],a[minindex]=a[minindex],a[i]
print(a)