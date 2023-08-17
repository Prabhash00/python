import re
def isValid(MobileNumber):
    Pattern= re.compile("(^[789]\d{9}$)")
    return Pattern.match(MobileNumber)

MobileNumber=input("Enter Mobile Number: ")
if(isValid(MobileNumber)):
    print("Valid Number")
else:
    print("Invalid Number")

#Prabhash Singh
#Roll-Number-202010101150020