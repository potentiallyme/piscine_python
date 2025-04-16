def NULL_not_found(object: any) -> int:
    t = type(object)
    s = ''
    type_handlers = {
        type(None): 'Nothing',
        float: 'Cheese',
        int: 'Zero',
        str: 'Empty',
        bool: 'Fake',
        'fail': None
    }
    s = type_handlers.get(t, 'fail')
    if s == None:
        print('Type not found')
        return 1
    print(f'{s}: {object} {t}')
    return 0 


