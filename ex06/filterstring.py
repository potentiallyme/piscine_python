from ft_filter import ft_filter
import string
import sys


def filterstring(s, n):
    '''
    Prints a list of words, in a list, from input string s longer than len n.

    Args:
        s (string): string from which the words are evaluated
        n (int): length used to evaluate words

    Returns:
        None
    '''
    if any(c in string.punctuation for c in s) or not s.isprintable():
        print('There is punctuation or special characters in your string')
        return None
    print(list(ft_filter(lambda x: len(x) > int(n), s.split(' '))))


def main():
    try:
        assert len(sys.argv) == 3, 'the arguments are bad'
        assert sys.argv[1].isascii(), 'the arguments are bad'
        assert sys.argv[2].isdecimal(), 'the arguments are bad'
        filterstring(sys.argv[1], sys.argv[2])
    except AssertionError as e:
        print('AssertionError:', e)
    return 0


if __name__ == '__main__':
    main()
