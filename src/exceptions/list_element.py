"""Trying exception handling by asking User an index:
If index is found return the element, Otherwise show Exception 
"""
L1=[1,4,2,5,0,10000,"Some"]
try:
    n=int(input("Enter an Index to return: "))
    print(L1[n])

except IndexError as ie:
    print("Index Error Occurred: ",ie)
except ValueError as ve:
    print("Input Type Mismatched: ",ve)
except Exception as e:
    print(e)    
finally: 
    print("Execution Completed")