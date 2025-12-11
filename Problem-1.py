# Problem-1: Create a small calculator which performs operations such as     Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string


def calculator(a , b , operation):
    if operation == "+":
        return a+b
    elif operation =="-":
        return a-b
    elif operation == "/":
        if b==0:
            return "Division by zero "
        return a/b
    elif operation =="*":
        return a*b
    else:
        return "Error : Invalid Operation"
a = float(input("Enter first number (a): "))
b = float(input("Enter first number (b): "))
operation = input("Enter operation (+, -, *, /): ")
print(calculator(a,b,operation))