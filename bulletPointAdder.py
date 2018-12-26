#! python3

import pyperclip
text = pyperclip.paste()

newText = text.split('\n')

for i in range(len(newText)):
    newText[i] = '* ' + newText[i]

newText = ('\n').join(newText)
print(newText)

# pyperclip.copy(text)
