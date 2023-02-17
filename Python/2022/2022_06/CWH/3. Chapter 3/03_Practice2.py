letter = '''
Dear <|name|>,
you are selected!
<|date|>.
'''
name = input("Enter the name:\n ")
date = input("Enter the date:\n ")
letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)
print(letter)


#print(template.replace('<|name|>', name).replace('<|date|>', date))