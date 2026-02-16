# This is a function file, in this i will be writing many functions and use it as module somewhere else
def add(v1,v2):
    return v1+v2

def sub(v1,v2):
    return v1-v2

def mul(v1,v2):
    return v1*v2

def div(v1,v2):
    if v2==0:
        return None
    return v1/v2

def add_all(*args):
    return sum(args)
def print_info(**kwargs):
    print(kwargs)


#Non Local Example
count=3
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

#Global Example
count_1=4
def make_counter_1():

    def increment():
        global count_1
        count_1 += 1
        return count_1

    return increment


if __name__ =="__main__":
    add_result = add(10,12)
    print(f"Result of Addition is {add_result}")
    sub_result = sub(12,10)
    print(f"Result of Subtraction is {sub_result}")
    mul_res=mul(12,13)
    print(f"Result of Multiplication is {mul_res}")
    div_res=div(v2=10,v1=3)
    print(f"Result of Division is {div_res}")
    sum_of_all=add_all(4,5,6,2,4,55,1,2554,65,199)
    print(f"Sum of All Values are {sum_of_all}")
    print_info(name="Leo", age=21)
    non_local = make_counter()
    print(non_local())
    print(non_local())
    global_kw=make_counter_1()
    print(global_kw())
    print(global_kw())