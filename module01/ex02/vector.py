import sys

class Vector:
    def __init__(self, *arg):
        self.data = []
        self.size = 0
        if len(arg) > 2 or len(arg) < 1:
            sys.exit("Error")
        if len(arg) == 2:
            if not all(isinstance(val, int) for val in arg):
                sys.exit("Error")
            if arg[0] > arg[1]:
                sys.exit("Error")
            deb = float(arg[0])
            while deb < arg[1]:
                self.data.append(float(deb))
                deb += 1
                self.size += 1
        elif len(arg) == 1:
            if isinstance(arg[0], list):
                for elem in arg[0]:
                    self.data.append(float(elem))
                    self.size += 1
            elif isinstance(arg[0], int):
                val = float(0)
                while val < arg[0]:
                    self.data.append(val)
                    val += 1
                    self.size += 1
            else:
                sys.exit("Error")
    def __add__(self, num):
        newvector = Vector([])
        if isinstance(num, int):
            for value in self.data:
                newvector.data.append(value + num)
        elif isinstance(num, Vector) and self.size == num.size:
            i = 0
            for value in self.data:
                newvector.data.append(value + num.data[i])
                i += 1
        return newvector
    
    def __radd__(self, num):
        newvector = Vector([])
        for value in self.data:
            newvector.data.append(value + num)
        return newvector
    
    def __sub__(self, num):
        newvector = Vector([])
        if isinstance(num, int):
            for value in self.data:
                newvector.data.append(value - num)
        elif isinstance(num, Vector) and self.size == num.size:
            i = 0
            for value in self.data:
                newvector.data.append(value - num.data[i])
                i += 1
        return newvector
    def __rsub__(self, num):
        newvector = Vector([])
        for value in self.data:
            newvector.data.append(value - num)
        return newvector
    
    def __truediv__(self, num):
        newvector = Vector([])
        if isinstance(num, int):
            for value in self.data:
                newvector.data.append(value / num)
        elif num.size != self.size:
            sys.exit("Error")
        elif isinstance(num, Vector):
            i = 0
            for value in self.data:
                newvector.data.append(value / num.data[i])
                i += 1
        return newvector
    def __rtruediv__(self, num):
        newvector = Vector([])
        for value in self.data:
            newvector.data.append(value / num)
        return newvector

    def __mul__(self, num):
        newvector = Vector([])
        if isinstance(num, int):
            for value in self.data:
                newvector.data.append(value * num)
        elif num.size != self.size:
            sys.exit("Error")
        elif isinstance(num, Vector):
            i = 0
            dotprod = 0
            for value in self.data:
                dotprod += value * num.data[i]
                i += 1
            return dotprod
        return newvector
    def __rmul__(self, num):
        newvector = Vector([])
        for value in self.data:
            newvector.data.append(value * num)
        return newvector
    def __str__(self):
        newstring = ''
        for value in self.data:
            if not newstring:
                newstring = 'Vector [' + str(value)
            else:
                newstring += ', ' + str(value)
        if newstring:
            newstring += ']'
        return newstring

    def __repr__(self):
        newstring = ''
        for value in self.data:
            if not newstring:
                newstring = 'Vector([' + str(value)
            else:
                newstring += ', ' + str(value)
        newstring += '])'
        return newstring