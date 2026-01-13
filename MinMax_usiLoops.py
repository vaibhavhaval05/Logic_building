list = [5,3,9,2,8]
a  = b = list[0]
for num in list:
    if num > a:
        a = num
    if num < b:
        b = num
print("Minimum:", b)
print("Maximum:", a)
