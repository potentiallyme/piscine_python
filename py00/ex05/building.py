import sys
import string


def main():
    '''
    This function gives the length of the string and counts:
    - Uppercase letters
    - Lowercase letters
    - Punctuation marks (from string.punctuation)
    - Whitespaces
    - Digits (as integers)

    Args:
    - s (str): The string to analyze from user input sys.argv[1]

    Returns:
    - None: Prints results directly
    '''
    try:
        assert len(sys.argv) < 3, 'AssertionError: too many arguments'
        if len(sys.argv) == 2:
            s = sys.argv[1]
        else:
            s = input('Enter a text to count below:\n')
        upper = lower = space = punc = dig = 0

        for i in s:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isspace():
                space += 1
            elif i in string.punctuation:
                punc += 1
            elif i.isdigit():
                dig += 1

        print(f'The text contains {len(s)} characters:')
        print(f'{upper} upper letters')
        print(f'{lower} lower letters')
        print(f'{punc} punctuation marks')
        print(f'{space} spaces')
        print(f'{dig} digits')

    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
