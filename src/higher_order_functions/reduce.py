from functools import reduce

#Finding products
prod_list=[22,3,1]
print(reduce(lambda x,y :x*y, prod_list))

#Finding Maximum

max_list=[12,45,66,99,1024]
print(reduce(lambda i,y : i if i>y else y ,max_list))