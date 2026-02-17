def number_stream(limit):
    for i in range(limit):
        yield i * 10

stream = number_stream(7)
try:
    for value in stream:
        print(value)
    #print(list(stream))
except Exception as e:
    print(e)
gen = (x for x in range(5))
print(next(gen))
print(next(gen))
print(list(gen))