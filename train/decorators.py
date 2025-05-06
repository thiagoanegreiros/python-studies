def my_dec(func):
    def wrapper(*args, **kargs):
        print('before')
        print(f'This are the args {args} {kargs}')
        func(args[0], kargs['a'])
        print('after')
    return wrapper


@my_dec
def init(args, kargs):
    print(f'Shazam {args} - {kargs}')


init(1, 2, 3, a = 5, b = 2)
