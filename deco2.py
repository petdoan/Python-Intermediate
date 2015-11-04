
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: {}'.format(func.__name__))
        print('Positional arguments: {}'.format(args))
        print('Keyword arguments: {}'.format(kwargs))
        result = func(*args, **kwargs)
        print('Result: {}'.format(result))
        return result
    return new_function

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)


