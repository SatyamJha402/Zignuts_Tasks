def calc(num_1, num_2, operator):
    if operator == "+":
        return print(f"the sum is {num_1 + num_2}")
    elif operator == "-":
        return print(f"the subs is {num_1 - num_2}")
    elif operator == "*":
        return print(f"the mult is {num_1 * num_2}")
    else:
        return print(f"the division is {num_1 / num_2}")
    
num_1 = int(input("give 1st number: "))
num_2 = int(input("give 2st number: "))
operator = input("give the operation to perform: ")
calc(num_1, num_2, operator)