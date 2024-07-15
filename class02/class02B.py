def func_print(name):
    print(name)


name = input("enter name: ")
func_print(name)


def get_my_numbers(number):
    a = number ** 2
    b = number ** 0.5
    c = number % 2 == 0
    #return list([a, b, c])         # return result as 'list' object
    return a, b, c                  # returns result as 'tuple' object by default


result = get_my_numbers(76)
print(result)
print(type(result))
