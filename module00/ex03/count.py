import sys
import string

def text_analyzer(text=None):

    if len(sys.argv) > 1:
        sys.exit("ERROR")
    if text == None:
        text = input("What is the text to analyze?")
    if len(text) == 0:
        sys.exit("No text to analyse")
    min = 0
    maj = 0
    space = 0
    punc = 0
    for letter in text:
        if letter.islower():
            min += 1
        elif letter.isupper():
            maj+= 1
        elif letter.isspace():
            space += 1
        elif letter in (string.punctuation):
            punc += 1
            
    print(f'The text contains {len(text)} characters:\n'
          f'- {min} lower letters\n'
          f'- {maj} upper letters\n'
          f'- {punc} punctuation marks\n'
          f'- {space} spaces')