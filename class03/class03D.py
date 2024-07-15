try:
    1/0
except ZeroDivisionError as ex:
    print("Cannot divide by zero")
    print(f"Some Error: {ex.args}")
