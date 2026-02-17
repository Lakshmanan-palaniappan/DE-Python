import logging
from functools import wraps
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s",filename="log.txt",filemode='a')
logging.info("----- This is the Start of Division -----")
def division_checker(func):
    @wraps(func)
    def wrapper(num1, num2):
        try:
            if num1 < num2:
                num1, num2 = num2, num1
                return func(num1, num2)
        except Exception as e:
            logging.error(e)
            print(e)
    return wrapper

@division_checker
def division_function(num1, num2):
    """Divide two numbers safely, swapping if needed."""
    return num1 / num2

result = division_function(2, 15)
print(result)
logging.info("----- This is the End of Division -----")
