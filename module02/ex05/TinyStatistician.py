import math

class TinyStatistician:
    def __init__(self):
        pass

    def mean(array):
        if not array:
            return None
        new_array = 0
        for elem in array:
            new_array += float(elem)
        return new_array / len(array)

    def median(array):
        if not array:
            return None
        array.sort()
        if len(array) % 2 == 0:
            return float((array[int(len(array) / 2 - 1)] + array[int(len(array) / 2 )]) / 2)
        else:
            return float(array[int(len(array) / 2 - 1)])
    
    def quartile(array, num):
        if not (num == 25 or num == 50 or num == 75) or not array:
            return None
        array.sort()
        return float(array[int((len(array) / 100) * num)])

    def var(array):
        if not array:
            return None
        var = 0.0
        for elem in array:
            var += (elem - TinyStatistician.mean(array)) ** 2
        return float(var / len(array))

    def std(array):
        if not array:
            return None
        return math.sqrt(TinyStatistician.var(array))
