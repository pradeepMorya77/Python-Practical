print()
a = int(input("Enter First Number:: "))
b = int(input("Enter Second Number:: "))
print()

# Arithmetic Operators
print("Arithmetic Operators")
print(f"The Addition of {a} and {b} is {a+b}")
print(f"The Subtraction of {a} and {b} is {a-b}")
print(f"The Division of {a} and {b} is {a/b}")
print(f"The Multiplication of {a} and {b} is {a*b}")
print(f"The Reminder of {a} and {b} is {a%b}")

# Assignment Operators
print()
print("Assignment Operators")
a += b
print(f"The value of a += b is {a}")
a -= b
print(f"The value of a -= b is {a}")
a *= b
print(f"The value of a *= b is {a}")
a /= b 
print(f"The value of a /= b is {a}")
a %= b
print(f"The value of a %= b is {a}")

# Comparison Operators
print()
print("Comparison Operators")
print(f"The Number of {a} Less than {b} is {a<b}")
print(f"The Number of {a} Greater than {b} is {a>b}")
print(f"The Number of {a} Less than equal to {b} is {a<=b}")
print(f"The Number of {a} Greater than equal to {b} is {a>=b}")
print(f"The Number of {a} equal to {b} is {a==b}")
print(f"The Number of {a} not equal to {b} is {a!=b}")

# Logical Operator
print()
print("Logical OR Operator")
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)
print()

print("Logical And Operator")
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)
print()

print("Logical NOT Operator")
print("NOT of False is", not(False))
print("NOT of True is", not(True))