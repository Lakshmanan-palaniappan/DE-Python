import sys
import itertools
#normal_list=[num for num in range(1,1000000000)]

gen_list=(num for num in range(1,10000000000))

#print("Normal List Size: ", sys.getsizeof(normal_list))
print("Generator List Size: ", sys.getsizeof(gen_list))


print(list(itertools.islice(gen_list, 100)))
