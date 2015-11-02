
def outer():
    '''the next line gives us access to global x'''
    global x
    print("in outer(), global x =", x)
    x = 1

    def inner(x):
         '''this is NOT the global x!'''
         print("in inner(), local/param x =", x)
         x = 2 
         print("in inner(), local/param x =", x)

    print("before inner(), x =", x)
    inner(x)
    print("after inner(), x =", x)

x = 0
print("at program start, global x is", x)
outer()
print("after calling outer(), global x is", x)


