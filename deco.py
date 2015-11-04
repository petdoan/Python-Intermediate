
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: {}'.format(func.__name__))
        print('Positional arguments: {}'.format(args))
        print('Keyword arguments: {}'.format(kwargs))
        result = func(*args, **kwargs)
        print('Result: {}'.format(result))
        return result

    return new_function

def add_ints(a, b, foo = 'bar', datatype = 'int'):
    return a + b

print('Running plain old add_ints()')
print(add_ints(3, 5))

''' manual decorator assignment '''
cooler_add_ints = document_it(add_ints) 

print('Running cooler add_ints()')
cooler_add_ints(3, 5)



