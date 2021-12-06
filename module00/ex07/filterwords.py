import sys
import string

if len(sys.argv) != 3:
    sys.exit("Error1")
if not type(sys.argv[1]) == str:
    sys.exit("Error2")
try:
    sys.argv[2] = int(sys.argv[2])
    for char in string.punctuation:
        sys.argv[1] = sys.argv[1].replace(char, " ")
    newlist = list(sys.argv[1].split())
    i = 0
    while i < len(newlist):
        if len(newlist[i]) <= sys.argv[2]:
            newlist.pop(i)
        else:
            i += 1
    print(newlist)
except ValueError:
    sys.exit("Error3")