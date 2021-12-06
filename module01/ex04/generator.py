import random
import sys
from collections import OrderedDict

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if len(sys.argv) < 2 or len(sys.argv > 3):
        sys.exit("Error")
    if not isinstance(text, str) or not isinstance(sep, str):
        sys.exit("Error")
    opt = (None, 'unique', 'ordered', 'shuffle')
    if option not in opt:
        sys.exit("Error")
    res = text.split(sep)
    if option == 'unique':
        res = list(OrderedDict.fromkeys(res))
    elif option == 'ordered':
        res.sort()
    elif option == 'shuffle':
        for i in range(100):
            y = random.randint(0, (len(res) - 1))
            temp = res[y]
            res.pop(y)
            res.append(temp)
    for elem in res:
        yield elem
