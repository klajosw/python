'''Fancier format string example with 
parameter identification numbers
-- useful when some parameters are used several times.'''

x = int(input('Enter an integer: '))
y = int(input('Enter another integer: '))
formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'
equations = formatStr.format(x, y, x+y, x*y)
print(equations)
