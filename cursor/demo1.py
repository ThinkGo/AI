# write a program for digital calculator

def calculator():
    print("Simple Digital Calculator")
    print("Operations: +, -, *, /")
    
    # Get input from user
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
    
    # Perform calculation based on operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operator!"
    
    return f"{num1} {operator} {num2} = {result}"

# Run the calculator
if __name__ == "__main__":
    print(calculator())
