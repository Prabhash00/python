'''
Python program to print all even numbers in a range
Prabhash Singh
202010101150020
'''
range1 = int(input("Enter starting limit of range: "))
range2 = int(input("Enter end limit of range: "))

for num in range(range1 , range2 + 1):
  if num % 2 == 0:
    print(num , end =" ")

