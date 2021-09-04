# num=int(input("enter a number ::"))
# if num%2==0:
#     print("not")
# else:
#     print("prime")


a=int(input("enter ::"))
flag=0
if a>1:
    for num in range(2,a):
        if a%num==0:
            break
    else:
        flag=1
if flag==1:
    print("prime")
else:
    print("not prime")
