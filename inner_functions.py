def outer():
    msg = "Python"
    x = 1

    def inner():
        print(f'{msg} is really cool!')
        nonlocal x
        x += 1
        print(x)

    return inner

fn = outer()
fn()
print(fn.__code__.co_freevars)