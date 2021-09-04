a=input("enter a sring :")
b=" "
for i in a:
    if i not in b:
        b=b+i  #b=ap
    else:
        print("first recursive character in ",a,"is",i)