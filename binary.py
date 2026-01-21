a = [3, 6, 9, 12, 15, 18, 21, 24]
find = 15
flag=False

l=0
h=7
while l<=h:
    mid=(l+h)//2
    if a[mid]==find:
        flag=True
        print("element is found..",mid)
        break
    elif a[mid]<find:
        l=mid+1
    else:
        h=mid-1
if not flag:
    print("not found")