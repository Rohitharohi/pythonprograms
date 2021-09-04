import re

x=input("enter registartion number ::")
a="[K][L]\d{2}[A-Z]{2}\d{4}$"
m=re.fullmatch(a,x)
if m is not None:
    print("valid")
else:
    print("invalid")