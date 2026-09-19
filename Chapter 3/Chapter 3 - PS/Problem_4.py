# Replace the double space from problem 3 with single spaces.
str = input("Enter string with double space: ")
print(f"Double space found at index {str.find("  ")}")

print(f"\nThis string is without double space is {str.replace("  ", " ")}")