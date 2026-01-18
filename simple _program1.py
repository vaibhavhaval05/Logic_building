#Write a program to check whether a number is divisible by 5.
#Write a program to check whether a number is divisible by 3 and 7.
#Write a program to check whether a character is a vowel or consonant.
#Write a program to check whether a number is 1-digit, 2-digit, or 3-digit.
#Write a program to check whether a character is uppercase or lowercase.
#Write a program to find the grade based on marks.
#Write a program to check whether a number is prime or not.
#Write a program to check whether a number is palindrome.
#Write a program to check whether a number is Armstrong.
#Write a program to find the smallest of three numbers

num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Number is divisible by 3 and 7")
else:
    print("Number is not divisible by 3 and 7")


ch = input("Enter a Character")

if ch in "aeiouAEIOU":
    print("this is vowel")
else:
    print("this is constant")

num = int(input("Enter a number: "))
   # handle negative numbers

if num < 10:
    print("1-digit number")
elif num < 100:
    print("2-digit number")
elif num < 1000:
    print("3-digit number")
else:
    print("More than 3-digit number")



marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D")
else:
    print("Grade: Fail")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest number is:", a)
elif b <= a and b <= c:
    print("Smallest number is:", b)
else:
    print("Smallest number is:", c)



