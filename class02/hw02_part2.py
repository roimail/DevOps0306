
# Question H,I
# ==============================================================
def get_name(sname: str):
    print(sname)

def get_number(fnumber: float):
    print(fnumber/2)

def add_numbers(num_a: float, num_b: float):
    return num_a + num_b

def add_strings(first_string: str, second_string: str):
    return first_string + " " + second_string
# ==============================================================

get_name(str("My Name"))
get_number(float(41.2))

numbers_sum = add_numbers(float(3), float(7.1))
print(numbers_sum)

spaced_string = add_strings("First", "Second")
print(spaced_string)
# ==============================================================


# Question K
# ==============================================================

# one loop
n = 5
for i in range(n):
    print('*' * (i+1))
print()

# two loops
for i in range(n):
    for j in range(i+1):
        print('*', end='')    # the end='' will prevent a newline after each * char
    print()

print()
# =============================================================


# Question L
# ==============================================================
n = 7
for i in range(1, 2*n):
    for j in range(1, 2*n):
        if (i == j) or (i+j == 2*n): print('*', end='')
        else: print(' ', end='')
    print()

# Question M
# ==============================================================
# seems either too simple of I misunderstand the phrasing
# ==============================================================