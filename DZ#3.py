def type_logger(func):
    def tag_wrapper(*args, **kwargs):
        print(','.join(f'{i}: {type(i)}' for i in args))

        return func(*args, **kwargs)

    return tag_wrapper

@type_logger
def calc_cube(*x):
   return x ** 3


username_f = calc_cube(2, 2)