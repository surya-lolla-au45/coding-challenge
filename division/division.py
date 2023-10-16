def division(dividend,divisor):
    if(dividend<divisor):
        print(error)
    else:
            print(dividend//divisor)
            print(dividend %divisor)
x=int(input("Enter the first number= "))
y=int(input("Enter the second number= "))
division(x,y)
