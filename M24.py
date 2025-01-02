x=float(input("Give your first input: "))
y=float(input("Give your second input: "))
is_on = True

def addition():
    summation = x+y
    return summation
def minus():
    devide = x-y
    return devide
def multiple():
    gun = x*y
    return gun
def devition():
     vhag = x/y
     return vhag
    
def user():
    user_1 = input("do you want to continue Y/N  : ").lower()
    return user_1

is_on = True

while is_on:
    z=input("Which operation do you want to do?" '+,-,*,/ :')
    if z == '+':
        print(addition())
        user_input = user()
        if user_input == "y":
            is_on = True
        elif user_input == "n":
            is_on = False
    elif z == '-':
        print(minus())
        user_input = user()
        if user_input == "y":
            is_on = True
        elif user_input == "n":
            is_on = False
    elif z == '*':
        print(multiple())
        user_input = user()
        if user_input == "y":
            is_on = True
        elif user_input == "n":
            is_on = False
    elif z == '/':
        print(devition())
        user_input = user()
        if user_input == "y":
            is_on = True
        elif user_input == "n":
            is_on = False
    else:
        print("invalid input")
        print(z)
