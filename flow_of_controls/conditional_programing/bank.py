amount=5000
withdraw=int(input("enter amount to withdraw :"))
if withdraw>amount:
    print("insufficient balance")
else:
    print("your current balance is :",amount - withdraw)