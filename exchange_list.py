"""a = [1,2,3,4,5]
a.insert(2,10)
print(a)"""

a = [1,1,2,3,2,3]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

