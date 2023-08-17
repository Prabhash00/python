import re

def main():
    password=input("Enter password having atleast 1 number, 1 special character, 1 caps letter and 1 small letter:\n")
    reg="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%#?&])[A-Za-z\d@$!#%*?&]{6,28}$"

    pat=re.compile(reg)
    mat=re.search(pat, password)

    if mat:
        print("Password is valid.")
    else:
        print("Password is invalid")

if __name__=='__main__':
    main()