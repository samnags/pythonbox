birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name to determine bday')
    name = raw_input()
    if name == '':
        break
    
    if name in birthdays:
        print('The birthday of ' + name + ' is ' + birthdays[name])
    
    else:
        print('No birthday for ' + name + 'What\'s their birthday?')
        bday = raw_input()
        birthdays[name] = bday
        print('Added')
        print birthdays