# x='[abc]' either a b or c
# x='[^abc]' except abc
# x='[a-z]' a to z
# x='[A-Z]' A to Z
# x='[a-zA-Z]' both lower and upper case are checked
# x='[0-9]' check digits
# x='[^a-zA-Z0-9]' special symbols
# x='\s' check space
# x='\d' check the digits
# x='\D' except digits
# x='\w' all words except special characters
# x='\W' for special characters





# quantifiers
# x='a+'  a including group
# x='a*' count including zero number of a
# x='a?' count a as each including zero no of a
# x='a{2}' 2 no of a position
# x='a{2,3}' minimum 2 a and maximum 3 a
# x='^a'  check starting with a
# x='a$' check ending with a




# import re
# count=0
# matcher=re.finditer('ab','aabbab')
# for i in matcher:
#     count+=1
# print("count=",count)


# import re     ## a including grp
#
# x="a+"
# matcher=re.finditer(x,"aaa aa gf")
# for match in matcher:
#     print("available at :",match.start())
#     print("match group :",match.group())


# import re
# count=0
# matcher=re.finditer('ab','ababbab')
# for i in matcher:
#     print(" i available at :",i.start())   ##return position..0,1,2
#     print("group :=",i.group())            ##which object find match
#     count+=1
# print("count =",count)



# import re
#
# x="[abc]"
# matcher=re.finditer(x,"abt_c?@5fhgf")
# for match in matcher:
#     print("available at :",match.start())
#     print("match group :",match.group())




# import re
#
# x="[^abc]"
# matcher=re.finditer(x,"abt_c?@5fhgf")
# for match in matcher:
#     print("available at :",match.start())
#     print("match group :",match.group())


# import re
#
# x="[a-zA-z]"
# matcher=re.finditer(x,"abt_c?@5fhGJYgf")
# for match in matcher:
#     print("available at :",match.start())
#     print("match group :",match.group())



# import re

# x="[^0-9a-zA-Z]"
# matcher=re.finditer(x,"abt_c?@LhHgf")
# for match in matcher:
    # print("available at :",match.start())
    # print("match group :",match.group())



# import re
#
# x="\W"
# matcher=re.finditer(x,"abt_c?@5fhgf")
# for match in matcher:
#     print("available at :",match.start())
#     print("match group :",match.group())