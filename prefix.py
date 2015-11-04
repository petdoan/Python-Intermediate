
def add_prefix(string, prefix='foo_'):
    return prefix + string

s = input('Enter a string: ')
print(add_prefix(s))
print(add_prefix(s, 'dive_'))

'''These examples fail because we are passing a positional
argument (s) after a keyword argument.

print(add_prefix(prefix='sand_', s))
sorted(reverse=True, list)
'''

'''Once a keyword argument is passed, ALL arguments following
must be keyword arguments'''

print(add_prefix(prefix='sand_', string=s))



