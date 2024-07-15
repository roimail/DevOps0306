
# Questions 1, 2, 6
# ======================================================================
try:
    1/0
except ZeroDivisionError as err:
    print(f"Error: {str(err)}\n")
    # ZeroDivisionError obviously catches errors related to division by zero

try:
    f = open('imaginary_file.txt', 'r')  # opening a file that does not exist
except IOError as err:
    print(f"Error: {str(err)}\n")
    # IOError will catch a collection of input/output errors, related to
    # opening/closing a file for reading/appending/writing, etc
# f.close()
# ======================================================================

# Question 3, 4, 5
# ======================================================================
# Yes of course the code is legal, it just makes no sense.
# There are so many exceptions in python, "Except:" catches all.
# I'm not going to list all of them, what is the point of this?
# This will not differentiate between distinct error types.
# ======================================================================


# Question 7, 8, 9, 10
# ======================================================================
def create_empty(file_name: str):
    try:
        fx = open(file_name, 'x')
    except FileExistsError:
        print(f"File {file_name} already exists")
    else:
        print(f"File {fx.name} was created")
        fx.close()

def add_line(file_name: str, line_text: str):
    try:
        fw = open(file_name, 'a')
    except BaseException as err:
        print(f"Error: {str(err)}")
    else:
        fw.write(line_text)
        fw.close()

def read_file(file_name: str):
    try:
        fr = open(file_name, 'r')
    except BaseException as err:
        print(f"Error: {str(err)}")
    else:
        print(fr.read(), end='')
        fr.close()
# ======================================================================

file_name='words.txt'
create_empty(file_name) # create an empty file
add_line(file_name, "Yet another line\n") # add a line to the file
add_line(file_name, "פיצה ספגטי גלידה\n") # add a line with hebrew text
read_file(file_name) # read the file
# ======================================================================
