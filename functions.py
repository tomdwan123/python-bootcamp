# format
def my_function():
    print("Hello Python")
    x = 3
    print(x ** x)

my_function()

# docstring
def say_hello(name):
    """This function says hello to you!"""
    print(f'Hello {name}!')

say_hello("Tony")
help(say_hello)
print(say_hello.__doc__)

# positional and keyword arguments
def difference(a, b):
    result = a - b
    print(result)

difference(1, 5)

def func1(x, y, z):
    print(f'1st parameter x is {x}')
    print(f'2nd parameter y is {y}')
    print(f'3rd parameter z is {z}')

func1(1, 2, 3)
func1(y = 5, x = 9, z = 3)

# default arguments
def add(x, y = 10):
    print(f'x is {x} and y = {y}')
    print(f'{x} + {y} = {x + y}')

add(2, 3)
add(6)

# return statement
def add1(a, b):
    return a + b;

def add2():
    pass

print(add1(1, 2))
print(add2()) # None

def my_func(x):
    return x, x**2, x**3, x**4

print(my_func(3))
a, b, c, d = my_func(10)
print(a, b, c, d) # 10 100 1000 10000

x, *y = my_func(4)
print(x, y) # 4 [16, 64, 256]

# variable-length arguments
def average(a, b, *args):
    print(f'args is {args}')
    return (a + b +sum(args)) / (2 + len(args))

print(average(4, 5, 6, 7))

def concatenate(*args):
    result = ''
    for tmp in args:
        result += tmp
    return result

result = concatenate('I', 'Love', 'Python')
print(result)

def my_funtion(**args):
    print(args)
    for k, v in args.items():
        print(f'k is {k} and v is {v}')

my_funtion(name='John', age=40, location='London')
person = {'name': 'Andrew', 'age': 30}
my_funtion(**person)

def connect(ip, port, username, password):
    print(ip, port, username, password)

server = {'ip': '172.0.0.1', 'port': 22, 'username': 'admin', 'password': '12345'}
connect(**server)

# scopes and namespaces
x = 10
y = 10
def my_func1():
    x = 5
    print(f'x inside the function: {x}')

my_func1()
print(f'x outside the function: {x}')

def my_func2():
    global y
    y += 1
    print(f'y inside the function: {x}')

my_func2()
print(f'y outside the function: {x}')

numbers = [1, 2, 3]
z = 10

def my_func3(numbers, z):
    numbers.append(4)
    z = 66
    print(f'z inside the function : {z}')

my_func3(numbers, z)
print(f'After calling the function, number is {numbers} and z is {z}')

x = 2

# lamda
def my_func(x, fn):
    return fn(x)


result = my_func('5', lambda x: x * 3)
result1 = my_func(5, lambda x: x * 3)
print(result) # 555
print(result1) # 15