# a=float(input("enter first number:"))
# b=float(input("enter second number:"))
# try:
#     res=a/b
#     print(res)
# except:
#     print("exception occured ....")

list=[1,2,3,4,5,6]
num=int(input("enter a index:"))
try:
    print(list[num])
except:
    print("index out of range")