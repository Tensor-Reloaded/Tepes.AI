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


def time_checker(func):
    import time

    def wrapped(*args, **kwargs):
        t1 = time.process_time()
        func(*args, **kwargs)
        t2 = time.process_time() - t1
        print('{} ran in: {} sec'.format(func.__closure__[0].cell_contents, t2))

    return wrapped


def exception_checker(func):
    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)

        except:
            print('{} function run with an exception!'.format(func.__closure__[0].cell_contents.__closure__[0].
                                                              cell_contents))
        else:
            print('{} function run with no exceptions!'.format(func.__closure__[0].cell_contents.__closure__[0].
                                                               cell_contents))

    return wrapped
