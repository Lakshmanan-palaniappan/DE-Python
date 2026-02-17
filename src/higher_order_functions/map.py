#Converting a list of strings into a list of their lengths
og_list=["Toyota","Nissan","Suzuki","Mahendra","Tesla","Tata"]

len_list=list(map(lambda x:len(x),og_list))
print(len_list)

#Squaring each number in a list
sq_list=[2,9,4,12,32,923,987]
print(list(map(lambda i:i*i,sq_list)))

