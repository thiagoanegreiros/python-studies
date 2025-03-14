def my_dec(func):
    def wrapper(*args):
        print(f'The args are {args}')
        func(*args)
    return wrapper

@my_dec
def my_func(*args):
    print(f'this is from inside the function {args}')

my_func(1, 2, 3)
