f = open("data.txt", "w")
f.write("Hello Vaibhav")
f.close()

f = open("data.txt", "r")
print(f.read())
f.close()

f = open("data.txt", "a")
f.write("\nLearning file handling")
f.close()
