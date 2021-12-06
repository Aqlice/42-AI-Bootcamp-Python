import sys

if len(sys.argv) != 2:
    sys.exit("ERROR")
try:
    a = int(sys.argv[1])
    if a == 0:
        sys.exit("I'm Zero.")
    elif int(a) % 2 == 0:
        sys.exit("I'm Even.")
    else:
        sys.exit("I'm Odd.")
except ValueError:
    sys.exit("ERROR")