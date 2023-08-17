import re

def isValid(PinCode):
    Pattern=re.compile("^[1-9]{1}[0-9]{2}\s{0,1}[0-9]{3}$")
    return Pattern.match(PinCode)

PinCode=input("Enter 6-digit Pin-Code :")
if(isValid(PinCode)):
    print("Valid Pincode :" + PinCode)
else:
    print("Invalid Pincode ")

#Prabhash Singh
#Roll-Number-202010101150020