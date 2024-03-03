l1 = [1, 2.5, True, "Hello", [1, 2, 3], (1, 2, 3)]
l2 = []
l3 = list()
print(len(l1))
print(l1[0])
print(l1[-1])

l1 = [3, 4]
print(l1, id(l1))
l1 = l1 + [5, 6]
print(l1, id(l1))
l1.extend([7, 8])
print(l1, id(l1))

# append() and extend()
l1.append(['a', 'b']) # [3, 4, 5, 6, 7, 8, ['a', 'b']]
print(l1)
l1.extend(['x', 'y']) # [3, 4, 5, 6, 7, 8, ['a', 'b'], 'x', 'y']
print(l1)

# slicing
numbers = [1, 2, 3, 4, 5]
num = numbers[1:4]
print(numbers)      # [1, 2, 3, 4, 5]
print(num)          # [2, 3, 4]
print(numbers[:3])  # [1, 2, 3]
print(numbers[2:])  # [3, 4, 5]
print(numbers[1:5:3]) # [2, 5]
print(numbers[4:1:-2]) # [5, 3]
print(numbers[::])     # [1, 2, 3, 4, 5]
print(numbers[::-1])   # [1, 2, 3, 4, 5]