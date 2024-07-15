def get_user_age():
    age = int(input("enter your age: "))
    if age > 120 or age < 0:
        #raise ValueError("Invalid age, must be between 1 and 120", age)
        return -1
    return age

def get_user_gender():
    gender = input("Enter gender: ")
    if gender == "M":
        return "Male"
    if gender == "F":
       # return "Female"
        return "Male"
    if gender == "Apache":
        return "Apache"