import sys


def whatis():
    try:
        assert len(sys.argv) > 1, 'please enter an argument'
        assert len(sys.argv) < 3, 'more than one argument is provided'
        av1 = sys.argv[1]
        assert av1.lstrip('-').isnumeric(), 'argument is not an integer'
        if int(av1) % 2 == 0:
            print('I\'m Even.')
        else:
            print('I\'m Odd.')
    except AssertionError as e:
        print('AssertionError:', e)


whatis()
