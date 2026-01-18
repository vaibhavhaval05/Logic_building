#Write a program to print Hello, Python!
#Write a program to take a name from user and print it.
#Write a program to take two numbers and print their sum.
#Write a program to take a number and print its square.
#Write a program to check whether a number is positive or negative.
#Write a program to check whether a number is even or odd.
#Write a program to take age and check if eligible to vote.
#Write a program to convert Celsius to Fahrenheit
#Write a program to take 3 numbers and print the largest.
#Write a program to check whether a year is a leap year.

print("hello,World")

name = (input("Write a name"))
print("your name is",name)

a = int(input("enter first num"))
b = int(input("enter second number"))

print("addition is",a+b)

name = (input("Write a number"))

if a>0:
    print("number is positive")
elif a<0:
   print("number is negative")
else:
    print("number is zero")

a = int(input("enter any num"))

if a % 2 ==0:
  print("even number")
else :
   print("number is odd")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if b > c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)








