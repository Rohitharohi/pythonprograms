x=5

def foo():
    global x
    x=x+10
    print("local x:",x)

foo()
print("global x:",x)

#we can define more variables inside "global" by using " , "

x=3
y=5

def glob():
    global x, y
    a = x ** 2
    b = x * y
    print("")