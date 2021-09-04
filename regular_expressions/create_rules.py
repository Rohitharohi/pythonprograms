# import re
#
# x="hello"
# a="[a-z]+"
# m=re.fullmatch(a,x)
# if m is not None:
#     print("valid")
# else:
#     print("invalid")




# import re
#
# x="56kg"
# a="[0-9]{2}[k][g]"
# m=re.fullmatch(a,x)
# if m is not None:
#     print("valid")
# else:
#     print("invalid")



import re

x=input("enter num to validate :")
a='\d{10}'
m=re.fullmatch(a,x)
if m is not None:
    print("valid")
else:
    print("invalid")