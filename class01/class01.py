
quit()

print("I am a string")

# Object types
listA = [1, "miao", True]              # list type object
print(listA[2])
d = {True: "roy", False: "something"}  # dictionary type object
print(d.keys())
print(d.values())

# different ways to concatenateEnter age:  strings
str1 = "hi"
str2 = "bye"
print(str1 + " " + str2)
print("%s %s" % (str1, str2))


age = int(input("Enter age: "))   # user input for age, converted to string
print(age,str(age))

# shortcuts:
# Shift+F10     run the code
# Alt+4         jump to the run windows
# Alt+2         break the code

# some notes
# aviel's email aviel33@gmail.com
'''test 1 2 3'''   # <--- this is also a way to mark out text

# if statement definition
if age == 20:
    print("yes")
elif age > 20:
    print("larger")
elif age < 20:
    print("smaller")
else:
    print("no")

# if statement in one line
if age == 20: print("yes")