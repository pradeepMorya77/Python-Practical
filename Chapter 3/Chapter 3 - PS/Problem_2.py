# Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Pradeep Morya").replace("<|Date|>", "10 january 2007")) 