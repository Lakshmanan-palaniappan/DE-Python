#Filtering only even from a list

given_list=[25,21,24,68,98,33,76]
print(list(filter(lambda x: x%2==0,given_list)))

#Keeping words of length >3
l1=["cat", "dog", "elephant", "rat", "lion"]
print(list(filter(lambda x: len(x)>3,l1)))