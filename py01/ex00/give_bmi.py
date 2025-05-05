import numpy as np


def give_bmi(height: list[float], weight: list[float]) -> list[float]:
    '''
    Takes two lists (heights and weights) and calculates BMIs

    Args:
        height (list): height values, preferably as floats
        weight (list): weight values, preferably as floats

    Returns:
        list created from array of calculated BMIs comparing both lists
    '''
    try:
        assert len(height) == len(weight), 'length of lists must match'
        h_arr = np.array(height)
        w_arr = np.array(weight)
        assert np.issubdtype(h_arr.dtype, np.number), 'heights must be numbers'
        assert np.issubdtype(w_arr.dtype, np.number), 'weights must be numbers'
        res = w_arr / (h_arr ** 2)
        return res.tolist()
    except AssertionError as e:
        print('AssertionError:', e)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    Takes a list of numbers and checks if they are above the given limit

    Args:
        bmi (list): values to check, must be numbers
        limit (int): limit values from list are compared to

    Returns:
        list created from array of compared values
    '''
    try:
        a = np.array(bmi)
        assert np.issubdtype(a.dtype, np.number), 'list must only contain nums'
        assert isinstance(limit, int), 'limit must be an integer'
        b = a > limit
        return b.tolist()
    except AssertionError as e:
        print('AssertionError:', e)
