import re

#Make a regular expression for validating an Email
regex='^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def check(email):
    if (re.search(regex, email)):
        print("Valid")
    else:
        print("Invalid ID")

if __name__== '__main__':
    email = input("Enter Email ID: ")
    check(email)