import sys

def check_list(my_list, my_tup=None):
    if all((isinstance(my_list, list), isinstance(my_tup, tuple))):
        if my_list[0]:
            if not len(my_list[0]) == my_tup[1]:
                sys.exit("Error, lists must be of equal sizes, and match the shape")
        i = 0
        for elem in my_list:
            if not isinstance(elem, list):
                sys.exit("Error, parameters should be list of list, tuple, or both")
            if len(elem) != my_tup[1]:
                sys.exit("Error, parameters should be list of list, tuple, or both")
            i += 1
        if i != my_tup[0]:
            sys.exit("Error, lists must be of equal sizes, and match the shape")
        return 1
    elif isinstance(my_list, list) and my_tup == None:
        y = 0
        #print(my_list)
        for elem in my_list:
            if len(elem) != len(my_list[0]):
                sys.exit("Error, lists must be of equal sizes, and match the shape")
            y+= 1
        return (y, len(my_list[0]))
    sys.exit("Error, parameters should be list of list, tuple, or both")

def create_matrix(my_tup):
    newlist = []
    for i in range(my_tup[0]):
        new = []
        for y in range (my_tup[1]):
            new.append(float(0))
        newlist.append(new)
    return newlist

def handle_add(self, num):
    if isinstance(num, Matrix) and self.shape == num.shape:
        newmatrix = Matrix(self.shape)
        if num.shape == self.shape:
            for i in range(num.shape[0]):
                for y in range(num.shape[1]):
                    newmatrix.data[i][y] = self.data[i][y] + num.data[i][y]
        return newmatrix
    sys.exit("Error, matrixes of same shapes only")

def handle_sub(self, num):
    if isinstance(num, Matrix) and self.shape == num.shape:
        newmatrix = Matrix(self.shape)
        if num.shape == self.shape:
            for i in range(num.shape[0]):
                for y in range(num.shape[1]):
                    newmatrix.data[i][y] = self.data[i][y] - num.data[i][y]
        return newmatrix
    sys.exit("Error, matrixes of same shapes only")

def handle_div(self, num):
    if isinstance(num, int):
        newrow = []
        for elem in self.data:
            newcolumn = []
            for number in elem:
                newcolumn.append(number / num)
            newrow.append(newcolumn)
        return(Matrix(newrow))
    sys.exit("Error, can only divide matrixes by scalars")

def handle_mul_scalar(self, num):
    newrow = []
    for elem in self.data:
        newcolumn = []
        for number in elem:
            newcolumn.append(number * num)
        newrow.append(newcolumn)
    return(Matrix(newrow))

def handle_mul_matrix(self, num):
    newvec = Matrix((self.shape[0], num.shape[1]))
    for row in range(self.shape[0]):
        for num_column in range(num.shape[1]):
            res = 0
            for column in range(self.shape[1]):
                res += self.data[row][column] * num.data[column][num_column]
            newvec.data[row][num_column] = res
    return newvec


class Matrix:
    def __init__(self, *arg):
        if len(arg) == 2:
            if check_list(arg[0], arg[1]):
                self.data = arg[0]
                self.shape = arg[1]
        elif len(arg) == 1:
            if isinstance(arg[0], list):
                self.data = arg[0]
                self.shape = check_list(arg[0])
            elif isinstance(arg[0], tuple):
                self.data = create_matrix(arg[0])
                self.shape = arg[0]
            else:
                sys.exit("Error, parameters should be list of list, tuple, or both")
        else:
            sys.exit("Error, parameters should be list of list, tuple, or both")
    
    def __add__(self, num):
        return handle_add(self, num)
    
    def __radd__(self, num):
        return handle_add(self, num)

    def __sub__(self, num):
        return handle_sub(self, num)

    def __rsub__(self, num):
        return handle_sub(self, num)
    
    def __truediv__(self, num):
        return handle_div(self, num)
    
    def __rtruediv__(self, num):
        sys.exit("Error, can only divide matrixes by scalars")
    
    def __mul__(self, num):
        if isinstance(num, int):
            return handle_mul_scalar(self, num)
        elif isinstance(num, Matrix):
            if self.shape[1] == num.shape[0]:
                return handle_mul_matrix(self, num)
        sys.exit("Error")

    def __rmul__(self, num):
        if isinstance(num, int):
            return handle_mul_scalar(self, num)
    def __str__(self):
        string = ''
        for row in self.data:
            string += str(row) + '\n'
        return f'matrix:\n{string[:-1]}'
    
    def __repr__(self):
        string = ''
        for row in self.data:
            string += str(row) + ','
        return f'Matrix([{string[:-1]}])'