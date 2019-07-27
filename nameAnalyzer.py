# nameAnalyzer.py
# 


name = input('Enter your full name: ')
print('Your name has', len(name),
      'characters (including spaces).')
print()

# break the name into its components
nameComponents = name.split(' ')
first = nameComponents[0]
last = nameComponents[-1]
numComponents = len(nameComponents)
print('Your name has', numComponents, 'components.')
print('  first name:', first)
print('   last name:', last)
if numComponents > 2:
    print(' other names:', ' '.join(nameComponents[1:-1]))
print()

# look for a letter within the name
letter = input('Enter a letter: ')
count = name.count(letter)
print('That letter occurs', count, 'times in your name.')
if count > 0:
    index = name.find(letter)
    print('The first occurrence is at position',
          index, 'in the name.')
    print('  before the first occurrence:', name[ :index])
    print('   after the first occurrence:', name[index + 1: ])
print()

# demonstrate two other string methods
print("Here's your name in all caps:", name.upper())
print("Here it is in all lower case:", name.lower())
