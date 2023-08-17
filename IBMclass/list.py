students= ["Prabhash", "Sid", "Fahad", "Hrithik","Harshit", 34,54,76,234]
numbers= [34,254,23,53,25,65] #list- muttable
#print(students)
print(students[3])
print(students[3:8]) #neglects the last digit of the entered limit
#numbers.sort()    -
#numbers.reverse() - these both change the original values of list
print(numbers, "num")
print(numbers[1:5])
print(numbers[2::3])
print(numbers[::-3],"reverse")
numbers.append(55343)
print(numbers)
numbers.remove(53)
numbers.pop()  #used to remove last number in list
print(numbers)
tuple1=(23,4354,54,7657,44,34,657,234)  #tuple- immutable
print("Tuple-", tuple1)
a,b=7,6
a,b=b,a    #swapping numbers
print(a,b)
A="the world is a happy place"
print(A[-8:-1])