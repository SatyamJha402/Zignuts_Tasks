def calculator():
    print("Calculator opened")
    
    while True:
        expr = input("Enter expression: ")

        if expr.lower() == 'q':
            print("Calculator closed")
            break
        
        try:
            allowed_chars = "0123456789+-*/()."
            if all(c in allowed_chars for c in expr):
                result = eval(expr)
                print("Result:", result)
            else:
                print("Invalid characters")
        except ZeroDivisionError:
            print("Zero division error")
        except Exception:
            print("Invalid expression")
            
            
calculator()