list = [1,1,0,1,1,1,0,1,1,1,1]
new_list = []
count = 0
for item in list:
    if item == 1:
        count += 1
    else:
            new_list.append(count)
            count = 0

new_list.append(count)
print(max(new_list))
