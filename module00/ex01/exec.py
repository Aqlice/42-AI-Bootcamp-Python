import sys

a = " ".join(sys.argv[1::])
print(a[::-1].swapcase())