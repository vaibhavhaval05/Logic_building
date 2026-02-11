a=[4,6,1,8,2,4]
un=[]
i=0
while i< len(a):
    if a[i] not in un:
        un.append(a[i])
    i=i+1
print(un)
