def product(*args):
    '''Return the product of the args passed in'''
    product = 1
    for term in args:
        result *= term
    return result
