def val_checker(check_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in args:
                if check_func(i):
                    return func(*args, **kwargs)
                else:
                    raise ValueError(f'ValueError: wrong val {i}')
        return wrapper
    return decorator



@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(-12)
print(a)