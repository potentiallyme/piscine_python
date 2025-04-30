import re
import sys


# For ease of use, dict is included in the file directly
NESTED_MORSE = {
        ' ': '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        }


def sos(s):
    '''
    Prints the input string translated into morse code.
    The string must contain only alphanumeric values and spaces.
    Spaces are represented as '/'.

    Args:
        s (string): string to be translated.

    Returns:
        None.
    '''
    try:
        assert re.fullmatch(r'[a-zA-Z0-9 ]+', s), 'the arguments are bad'
        print(' '.join(NESTED_MORSE[c.capitalize()] for c in s))
    except AssertionError as e:
        print('AssertionError:', e)


def main():
    try:
        assert len(sys.argv) == 2, 'Syntax: python sos.py [string]'
        sos(sys.argv[1])
    except AssertionError as e:
        print('AssertionError:', e)


if __name__ == '__main__':
    main()
