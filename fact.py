
def fact(n):
    '''returns n!'''
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

