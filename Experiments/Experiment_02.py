# To write a Python program to demonstrate a basic calculator using arithmetic operators.

a = float(input("Enter First Number:: "))
b = float(input("Enter Second Number:: "))

print("\n----Menu----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter Your Choice (1-4):: "))

if choice == 1:
    print(f"Addition of {a} and {b} is {a+b}")

elif choice == 2:
    print(f"Subtraction of {a} and {b} is {a-b}")

elif choice == 3:
    print(f"Multiplication of {a} and {b} is {a*b}")

elif choice == 4:
    if b != 0:
        print(f"Division of {a} and {b} is {a/b}")
    else:
        print("Cannot divide by zero")

else:
    print("Invalid Choice.")