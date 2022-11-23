def call_decorator(func):
    def wrapped(*args, **kwargs):
        print('Calling ##' + func.__name__ + '## with the following parameters: ')
        if len(args) == 0:
            print('No Parameters')
        else:
            for arg in args:
                print('Parameter: ' + str(arg), ' ')
        print()
        return func(*args, **kwargs)

    return wrapped
