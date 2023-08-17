'''
Name-  Prabhash Singh
Roll no.- 202010101150020
'''
arr=[10,18,6,348,329,34,123,999,10000]
m=0
n=int(input("Enter a number to searched from the array: "))
for i in range (len(arr)):
    if arr[i]==n:
        m=i
        break
if m>0:
    print("Number Found at: ", m)
else:
    print("Number not found")        