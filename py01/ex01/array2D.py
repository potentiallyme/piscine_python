import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Takes a list and slices it into the given size

    Args:
        family (list): original list to slice
        start (int): starting index
        end (int): ending index

    Returns:
        List created from sliced array
    '''
    try:
        assert isinstance(family, list), '1st param must be list'
        assert isinstance(start, int), '2nd param must be int'
        assert isinstance(end, int), '3rd param must be int'
        a = np.array(family)
        assert np.issubdtype(a.dtype, np.number), 'list must contain nums'
        print(f'My shape is: {a.shape}')
        b = a[start:end]
        print(f'My new shape is: {b.shape}')
        return b.tolist()
    except AssertionError as e:
        print('AssertionError:', e)
