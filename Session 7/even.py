def check(num):
    if(num < 0):
        return print("given number isn't valid")
    elif num % 2 == 0:
        return print("number is even")
    else:
        return print("given number is odd")
    
number = int(input("give a number to check: "))
check(number)