# Write the python code for digital calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b    

# take input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

if choice == '1':
    print(a,"+",b,"=", add(a,b))

elif choice == '2':
    print(a,"-",b,"=", subtract(a,b))

elif choice == '3':
    print(a,"*",b,"=", multiply(a,b))

elif choice == '4':
    print(a,"/",b,"=", divide(a,b))
else:
    print("Invalid input")
    