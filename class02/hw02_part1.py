# ==============================================================
# This function will force text input to be a number
def input_number(text_show):
    while True:
        try: n = float(input(text_show)); break
        except: print("Please enter a valid number")
    return n

# This function limit input string length to 'x' chars
def input_limit(show_text, x):
    while True:
        string_input = input(show_text)
        if len(string_input) == x: break
        else: print("Input incorrect")
    return string_input
# ==============================================================


'''
# Question A
# ==============================================================
X = input_number("Enter value for X: ")
Y = input_number("Enter value for Y: ")

if X > Y: print("X is larger than Y")
elif X < Y: print("X is smaller than Y")
elif X == Y: print("X is equal to Y")
# ==============================================================


# Question B
# ==============================================================
for i in range(5):
    print("Iteration number", i+1)
# ==============================================================


# Question C
# ==============================================================
n = input_number("Enter number between 1-4: ")
if n == 1: print("summer")
elif n == 2: print("winter")
elif n == 3: print("fall")
elif n == 4: print("spring""")
else: pass
# ==============================================================


# Question D
# ==============================================================
# The following loop will run 10 times
count = 1
while count < 11:
    print(count)
    count = count+1
# ==============================================================


# Question E
# ==============================================================
age = input_number("Your age: ")
ln = input_limit("First letter of your last name: ", 1)
usd_nis = input_number("Current shekel to dollar current: ")
abroad = input("Been to another country [True/False]: ")        # <--- update this
apt_number = input_number("Your apartment number: ")

print("age: ", age, "years\nFirst letter of last name:", ln)
print("age + currency (huh?) = ", age+usd_nis)
# ==============================================================


# Question F,H
# ==============================================================
phone_number = input("Enter phone number (numbers only): ")
print("You entered: ", phone_number)
# ==============================================================
'''
