import os

def load_file(file, base_path='/', mode='rb'):
    return open(os.path.join(base_path, file), mode)

f = load_file('example.txt')
f.mode
f.close()

import functools
load_writable = functools.partial(load_file, mode='w')
f = load_writable('example.txt')
f.mode
'w'
f.close()

