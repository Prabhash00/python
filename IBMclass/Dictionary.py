#Dictionary is key value pairs
d1={}
print(type(d1))
d2 = {"Prabhash":"Pizza","SHIELD":{"Harshit":"Burger",
"Sid":"Honey chili potato","Fahad":"Biryani","Hrithik":"Chai"}}

d2["Aman"]="Non-Veg"
d2["Mayank"]="kebab roll"
print(d2)
del d2["Mayank"]
print (d2["SHIELD"])
d3=d2.copy()
del d3 ["Prabhash"]
print(d2)