#Experiment :Write a program to check that a given year is Leap
#Year or not. Take input from user.
year= int(input("Enter year to check: "))

if(year%4==0 and year%100!=0 or year%400==0):
    print(year, "is a leap year")
else: 
    print(year, "is not a leap year")

'''
Name-  Prabhash Singh
Roll no.- 202010101150020
'''  