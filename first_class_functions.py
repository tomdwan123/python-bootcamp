def sum(x, fn):
    sum = 0

    for n in range(1, x + 1):
        sum += fn(n)
    return sum

def square(x):
    return x * x

print(sum(3, square)) # math.sqrt