# a=int(input("enter range :"))     ##*
# for i in range(0,a):              ##* *
#     for j in range(i):            ##* * *
#         print("*",end=" ")
#     print()   ##print("\r)


# a=int(input("enter range :"))
# for i in range(0,a):
#     num=1
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()   ##print("\r)


# k=3
# for i in range(0,6):
#     for s in range(0,k):
#         print(end=" ")
#     k=k+1
#     for j in range(0,6):
#         print("*",end=" ")
#         # k=k+1
#     print("\r")



# k=6
# for i in range(0,6):                  #row
#     for r in range(k):                #spacing
#         print(end=" ")
#     k=k-1
#     for j in range(0,i+1):              #star
#         print("*", end=" ")
#     print("\r")


def square(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end=" ")
        print("\r")
square(6)

for i in range(5,0,-1):     # i=5,4,3,2,1
    for j in range(0,i):    # j=0,1,2,3,4,5
        print("*",end=" ")  #i=5 j=0
    print("\r")