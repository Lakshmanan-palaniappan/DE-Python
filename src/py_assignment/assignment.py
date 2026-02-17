# This is the first question
import numpy
from datetime import datetime
import os
from collections import namedtuple
import calendar
if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command = input().split()
        operation = command[0]
        if operation == "insert":
            i, e = int(command[1]), int(command[2])
            my_list.insert(i, e)
        elif operation == "print":
            print(my_list)
        elif operation == "remove":
            e = int(command[1])
            my_list.remove(e)
        elif operation == "append":
            e = int(command[1])
            my_list.append(e)
        elif operation == "sort":
            my_list.sort()
        elif operation == "pop":
            my_list.pop()
        elif operation == "reverse":
            my_list.reverse()
# Find the Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{result:.2f}")
# Second Largest
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sec_max = sorted(set(arr))
    print(sec_max[-2])
# Mutation String


def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Merge the tools


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        seen = set()
        res = []
        for j in substring:
            if j not in seen:
                seen.add(j)
                res.append(j)
        print(''.join(res))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Python string formatting


def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number+1):
        print(
            f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].upper().rjust(width)} {bin(i)[2:].rjust(width)}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Text Alignment


thickness = int(input())  # This must be an odd number
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))


for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))


for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))


for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c +
          (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
# Calander module
i, j, k = map(int, (input().split()))
fdate = calendar.weekday(k, i, j)
print(calendar.day_name[fdate].upper())

# Named Tuple


n = int(input())
Student = namedtuple('Student', input().split())

total_marks = sum(int(Student(*input().split()).MARKS) for _ in range(n))
average = total_marks / n
print(f"{average:.2f}")

# Python time delta


# Complete the time_delta function below.

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    return str(abs(int((dt1 - dt2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# Floor-Ceil-Rint
numpy.set_printoptions(sign=' ')

A = numpy.array(input().split(), float)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

# np-min-and-max


n, m = map(int, input().split())

arr = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(numpy.max(numpy.min(arr, axis=1)))

# np-linear-algebra


n = int(input())

arr = numpy.array([list(map(float, input().split())) for _ in range(n)])

det = numpy.linalg.det(arr)

print(round(det, 2))

# mean-var-and-std

n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))
# No Idea!


def calculate_happiness(arr, set_a, set_b):
    happiness = 0
    for num in arr:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1
    return happiness


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    print(calculate_happiness(arr, set_a, set_b))
