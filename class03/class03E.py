def get_user_age():
    age = int(input("enter your age: "))
    if age > 120 or age < 0:
        #print("Sorry, you are too weird:")
        #return -1
        raise ValueError("Invalid age, must be between 1 and 120", age)
    return age

try:
    age = get_user_age()
except BaseException as e:
    print(e)