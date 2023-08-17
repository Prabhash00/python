#EXPERIMENT : Experiment 2:WAP to print 'n' terms of Fibonacci series 
# using iteration

n = int(input("Enter the value of 'n': "))
x = 0
y = 1
if n == 0 :
  print ("Fiboancci series:", x)
elif n==1:
  print("Fibonacci series:", y)
else:
  for i in range (1,n+1):
   print(x)
   add=x+y
   x=y
   y=add
   
'''
Name-  Prabhash Singh
Roll no.- 202010101150020
'''
   