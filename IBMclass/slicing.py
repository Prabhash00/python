newstr="My name is Prabhash"
#print(len(newstr))
print(newstr[:])
print(newstr[11:19])
print(newstr[11:19:2])
print(newstr[1::2])
print(newstr[-8:-1])
#STRING REVERSING
print(newstr[::-1])
print(newstr[::-2])

#boolean outputs
print("")
print(newstr.endswith("Prabhash"))
 
#others
print(newstr.count("h"))
print(newstr.lower())
print(newstr.upper())
print(newstr.replace("Prabhash", "Prishu"))

#NEVER TAKE -ve NUMBER MORE THAN -1 IN SLICING NUMBERS
