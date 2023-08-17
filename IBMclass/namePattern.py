string1=""
for i in range (9):
    for j in range (9):
        if (j==1 or ((i==0 or i ==3) and j>0 and j<5) or ((j==5 or j==1)and (i==1 or i ==2))):
            string1 = string1+"*"
        else:
           string1 = string1+" "
    string1 = string1+"\n"
print(string1)
