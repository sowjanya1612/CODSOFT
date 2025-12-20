def calculator():
    print("===== SIMPLE CALCULATOR =====")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nChoose operation:")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")
        
        choice = input("Enter operation (+, -, *, /): ")
        
        if choice == "+":
            print("Result:", num1 + num2)
        elif choice == "-":
            print("Result:", num1 - num2)
        elif choice == "*":
            print("Result:", num1 * num2)
        elif choice == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero is not allowed")
        else:
            print("Invalid operation selected")
    
    except ValueError:
        print("Please enter valid numeric values")

calculator()
