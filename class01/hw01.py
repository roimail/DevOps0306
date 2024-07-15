import time
import random

# Lesson 01, Homework set 01

# A
first = int(7)  # should automatically be defined as int
second = float(44.3)  # should automatically be defined as float

print(float(first) + second)  # I understand that the float() function here is redundant
print(float(first) * second)
print(second / float(first))

# B
# a will be equal to 9          (the last defined value in order)
# b will be equal to 8          (same reason)
# c wills be equal to 9+6=15    (same reason)


# C
# no functional difference between 'john' and "john"

my_number = 5 + 5
print("result: ", my_number)  # '+' sign was replaced with a comma ('+' inside print will add strings)

# D
x = 5
y = 2.36
print(x + int(y))  # result will be 7 because the int() function rounds down the y float variable

a = 8
b = "123"
print(a + int(b))
