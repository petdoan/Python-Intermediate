
'''This function takes 2 positional arguments, followed by 0+
keywords arguments.'''
def func1(pos1, pos2=1, **kwargs):
    print("pos1 =", pos1) 
    print("pos2 =", pos2)
    print("kwargs =", kwargs)

'''This function takes 2+ positional arguments, followed by 0+
keywords arguments.'''
def func2(pos1, pos2=1, *args, **kwargs):
    print("pos1 =", pos1) 
    print("pos2 =", pos2)
    print("args =", args)
    print("kwargs =", kwargs)


