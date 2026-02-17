def number_stream(limit):
    for i in range(limit):
        yield i * 10

stream = number_stream(7)
#print(list(stream))
try:
    for value in stream:
        print(value)
except Exception as e:
    print(e)