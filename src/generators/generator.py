def number_stream(limit):
    for i in range(limit):
        yield i * 10

stream = number_stream(7)
for value in stream:
    print(value)
