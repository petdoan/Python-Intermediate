import sys

from contextlib import redirect_stdout

print("before the with statement")

with redirect_stdout(sys.stderr):
    print("NOTE! the output of help goes to stderr")
    help(pow)

print("after the with statement")


