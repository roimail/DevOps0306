import time
import random

# First class
# A
first = int(7)                           # should automatically be defined as int
second = float(44.3)                       # should automatically be defined as float
print(float(first) + second)              # I understand the float() function here is redundant
print(float(first) * second)
print(second/float(first))

# B
# a will be equal to 9        (the last defined value in order)
# b will be equal to 8        (same reason)
# c wills be equal to 9+6=15   (same reason)

# C
# no functional difference between 'john' and "john"

print("roy" + "\t" + "something", end='')
print("\r\t\t")  # <--- this makes the text disappear because \r takes it backwards in text

print(random.randint(0, 100), end='')
time.sleep(1)
print("\r    ")
