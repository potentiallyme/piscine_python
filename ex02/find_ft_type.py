def handle_str(object):
    print(f'{object} is in the kitchen : {type(object)}')
def all_thing_is_obj(object: any) -> int:
    t = type(object)
    type_handlers = {
        str: handle_str,
        int: lambda val: print(f'Int : {t}'),
        float: lambda val: print(f'Float : {t}'),
        list: lambda val: print(f'List : {t}'),
        tuple: lambda val: print(f'Tuple : {t}'),
        dict: lambda val: print(f'Dict : {t}'),
        set: lambda val: print(f'Set : {t}')
    }
    type_handlers.get(t, lambda val: print('Type not found'))(object)
    return 42


