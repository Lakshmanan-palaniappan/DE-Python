lst1=[1,62,32]
lst1.extend([2,3])
slist=sorted(lst1)
print(slist)
print(lst1)
del lst1[1]
print(lst1)

d = {"name": "Leo", "age": 25}
for k,v in d.items():
    print(k,v)
print(d.items())

s={1,4,2,5}
t={1,2,7,8,9}
print(s.union(t))
print(s)
