import sys

alphabet = {'A': '.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
                'H': '....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
                'O': '---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
                'V': '...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', ' ': '/'}
alphabet.update({
    '0': '-----', '1': '.----',
    '2': '..---', '3': '...--',
    '4': '....-', '5': '.....',
    '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
})
string = ''
for elem in sys.argv:
    if elem == sys.argv[1]:
        string += elem
    elif elem != sys.argv[0]:
        string += ' ' + elem
string = string.upper()
newstring = ''
if all(x.isalnum() or x.isspace() for x in string):
    for x in string:
        newstring += alphabet[x] + ' '
else:
    sys.exit("Error")
print(newstring[:-1:])