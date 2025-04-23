import math


def NULL_not_found(object: any) -> int:
    type_handlers = {
        type(None): ('Nothing', lambda x: x is None),
        float: ('Cheese', lambda x: isinstance(x, float) and math.isnan(x)),
        int: ('Zero', lambda x: x == 0 and isinstance(x, int)),
        str: ('Empty', lambda x: x == ''),
        bool: ('Fake', lambda x: x is False)
    }
    for t, (label, checker) in type_handlers.items():
        if checker(object):
            print(f'{label}: {object} {type(object)}')
            return 0
    print('Type not found')
    return 1
