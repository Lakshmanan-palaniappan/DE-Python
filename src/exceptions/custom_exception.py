class NegativeNumberError(Exception):
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot take square root of a negative number")
    return num ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Error:", e)

