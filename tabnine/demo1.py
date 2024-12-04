 #Wtrite a function for addtion of two numbers
def add_numbers(a, b):
   return a + b 
#Wtrite a function for subtraction of two numbers
def subtract_numbers(a, b):
   return a - b


#Wtrite a function for multiplication of two numbers
def multiply_numbers(a, b):
   return a * b

#Wtrite a function for division of two numbers
def divide_numbers(a, b):
   # Check if the denominator is zero, if yes return an error message
   if b == 0:
       return "Error: Division by zero is not allowed."
   else:
       return a / b 


# Testing the above functions  
print(add_numbers(5, 3))  # Expected output: 8
print(subtract_numbers(5, 3))  # Expected output: 2
print(multiply_numbers(5, 3))  # Expected output: 15
print(divide_numbers(5, 3))  # Expected output: 1.6666666666666667
print(divide_numbers(5, 0))  # Expected output: Error: Division by zero is not allowed.

#/bin/sh: python: command not found
