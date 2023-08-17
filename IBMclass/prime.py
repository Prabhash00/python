#Experiment 2: WRITE A PYTHON PROGRAM TO FIND ALL PRIME
#NUMBERS WITHIN A GIVEN RANGE.
start= int (input("Enter the starting range: "))
end= int (input ("Enter the ending range: "))
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 

'''
Name-  Prabhash Singh
Roll no.- 202010101150020
'''
