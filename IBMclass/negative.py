'''
Python program to print all negative numbers in a range
Prabhash Singh
202010101150020
'''
num_start = int(input("Enter starting limit of range: "))
num_end = int(input("Enter end limit of range: "))

for num in range (num_start , num_end + 1):
    if num < 0: 
        print(num, end = " ") 
