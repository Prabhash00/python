'''
Python program to find second highest number
Prabhash Singh
Roll number- 202010101150020
'''
list1 = [10,18,94,7,38,67]
maximum=max(list1[0],list1[1]) 
secondmax=min(list1[0],list1[1]) 
n =len(list1)
for i in range(2,n): 
    if list1[i]>maximum: 
        secondmax=maximum
        maximum=list1[i] 
    elif list1[i]>secondmax and \
        maximum != list1[i]: 
        secondmax=list1[i]
 
print("Second highest number is : ",\
      str(secondmax))
