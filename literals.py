a=(False==0)
b=(True==1)
print(a)
print(b)

drink="pepsi"
food=None
def menu(x):
    if x==drink:
        print(drink)
    else:
        print(food)
menu(drink)
menu(food)