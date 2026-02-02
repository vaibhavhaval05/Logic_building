try :
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))
    print(a/b)

except(ZeroDivisionError,ValueError):
    print("enter proper value")

else:
    print("every thing is perfect")

finally:
    print("I will execute every time")
