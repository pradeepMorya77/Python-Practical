# To write a Python program to count the number of vowels and consonants in a given string.

text = input("Enter String:: ")

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aieou":
            vowels += 1
        else:
            consonants += 1

print(f"Number of Vowels is {vowels}")
print(f"Number of Consonants is {consonants}")