'''
Prabhash Singh
Roll No.-2020210101150020
'''
for num in range (1,2001):
  order = len(str(num))
  sum=0
  armno=num
  while armno>0:
    #for checking the entered number is armstrong or not
    digit= armno%10
    sum+=digit**order
    armno= armno//10
  if (num==sum):
    print(num)
