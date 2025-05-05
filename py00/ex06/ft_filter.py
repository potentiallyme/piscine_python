def ft_filter(f, it):
    '''
    Return an iterator yielding items from an iterable evaluated as truthy.

    Args:
        f (func): The function to apply to the items
        it (iterable): The iterable from which to yield the items

    Returns:
        iterator: The items (i) evaluating to true from f(i) or i if f is None.
    '''
    if not hasattr(it, '__iter__'):
        raise TypeError('Second argument  must be iterable')
    return (i for i in it if (i if f is None else f(i)))
