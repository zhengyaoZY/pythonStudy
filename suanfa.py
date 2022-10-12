import sys


# try to import the function plus from a_plus_b.py in the same directory
# - write your code here -
from a_plus_b import plus

# read two parameters from command like `python main.py 1 2` by sys.argv
# - write your code here -
a = int(sys.argv[1])
b = int(sys.argv[2])

# call plus function and add them up
# - write your code here -
c = plus(a, b)

# print the sum to the console
# - write your code here -
print(c)