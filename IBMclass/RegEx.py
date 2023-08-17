import re
name1= input("Enter the string: ")
print("The original string is :" +(name1))
if bool(re.match('[a-zA-Z\s]+$', name1)):
    print("Entered Name is Valid : " + str(name1)) 
else:
    print("Name is Not Valid")

#Prabhash Singh
#Roll-Number : 202010101150020