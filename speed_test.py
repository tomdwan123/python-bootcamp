from functools import wraps

# defining a decorator
def timer(fn):
    from time import time

    @wraps(fn)
    def wrapper_time(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'{fn.__name__} execution time: {end_time - start_time}')
        return result

    return wrapper_time

# decorating the function
@timer
def sum_of_powers(n, p):
    nums = [x ** p for x in range(1, n)]
    return sum(nums)

s = sum_of_powers(1000000, 2)
print(s)

s = sum_of_powers(1000000, 3)
print(s)

s = sum_of_powers(1000000, 5)
print(s)