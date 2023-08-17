n = int (input("Enter number of elements for the list "))
listb=[]
#for inputting the list
print("Enter the elements")
for i in range(0, n):
    elment = int(input())
    listb.append(elment)
for j in range(n):
    for k in range(0,n-1):
        if listb[k]>listb[k+1]:
         listb[k],listb[k+1]= listb[k+1],listb[k]
print("Sorted list: ", listb)
'''
Prabhash Singh
202010101150020
'''