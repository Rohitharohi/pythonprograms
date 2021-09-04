# # def div(num1,num2):
# #     return (num1/num2)
# # print(div(8,10))
#
#
#
# # ivde 1st num small ayal..oru fraction ahn kita...ingane varumbo valya value ethano
# # ath edth less ayit varuna valuene div cheyum....swap
#
#
# def revert_val(func):
#     def wrapper(no1,no2):   ##inner function...verim name kodkam.but ithan common
#         if no1<no2:
#             no1,no2=no2,no1
#             return func(no1,no2)
#         else:
#             return func(no1,no2)
#     return wrapper
#
# @revert_val
# def div(num1,num2):
#     return (num1/num2)
# print(div(5,10))






def admin_required(func):
    def wrapper(a,b):
        if a!="admin":
            raise Exception("you are not allowed")
        else:
            return func(a,b)
    return wrapper


@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_acc(user,acno):
    return str(acno)+"delete"
print(change_pin("admin",1000))
print(delete_acc("user1",1000))