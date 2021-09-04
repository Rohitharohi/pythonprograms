import re

x=input("enter a phone number ::")
a="[+][9][1]\d{10}$"
m=re.fullmatch(a,x)
if m is not None:
    print("valid")
else:
    print("invalid")