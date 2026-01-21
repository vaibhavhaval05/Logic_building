a = [5, 5, 5]
maxnum = max(a)

second_max = None
for i in a:
    if i != maxnum:
        if second_max is None or i > second_max:
            second_max = i

print("Max:", maxnum)
print("Second Max:", second_max)
