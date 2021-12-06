import sys

class Evaluator:
    
    def zip_evaluate(words, coefs):
        if not (isinstance(words, list) and isinstance(coefs, list)):
            sys.exit("Error")
        if not len(words) == len(coefs):
            return -1
        res = 0
        for word, coef in zip(words, coefs):
            res += len(word) * float(coef)
        return res
    
    def enumerate_evaluate(words, coefs):
        if not (isinstance(words, list) and isinstance(coefs, list)):
            sys.exit("Error")
        if not len(words) == len(coefs):
            return -1
        res = 0
        for i, word in enumerate(words):
            res += len(word) * float(coefs[i])
        return res