min=int(input("enter min :"))
max=int(input("enter max :"))
for num in range(min,max+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)