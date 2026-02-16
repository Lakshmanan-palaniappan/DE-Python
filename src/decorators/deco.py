def repeat(n):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return my_decorator

@repeat(5)
def add(a, b):
    return a + b

print(add(3, 4))
