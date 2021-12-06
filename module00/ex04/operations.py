import sys

if len(sys.argv) == 1 or sys.argv[1] == "usage":
    sys.exit("Usage : python operations.py <number1> <number2>")
if len(sys.argv) > 3:
    sys.exit("InputError, too many arguments")
if len(sys.argv) < 3:
    sys.exit("InputError, too few arguments")
if type(sys.argv[1] == str) or type(sys.argv[2] == str):
    sys.exit("InputError, plz only use numbers")
try:
    a = int(sys.argv[1]) 
    b = int(sys.argv[2])
    print(a + b)
    print(a - b)
    print(a * b)
    if b != 0:
        print(a / b)
    else:
        print("ERROR, div by zero")
    if b != 0:
        print(a % b)
    else:
        print("ERROR, modulo by zero")
except ValueError:
    sys.exit("InputError, plz only use numbers")
