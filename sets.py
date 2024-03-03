s1 = {1, 2, 'a', 10, 4, 'a', 2}
print(s1)

s1 = {1, 3, 5}
s2 = {5, 7, 9}

# intersection()
s3 = s1.intersection(s2)
print(f'set3: {s3}') # {5}
s3 = s1 & s2
print(f'set3: {s3}')  # {5}

# difference()
s4 = s1.difference(s2)
print(f'set4: {s4}') # {1, 3}
s4 = s1 - s2
print(f'set4: {s4}') # {1, 3}

# symmetric_difference()
s5 = s1.symmetric_difference(s2)
print(f'set5: {s5}')  # {1, 3, 7, 9}
s5 = s1 ^ s2
print(f'set5: {s5}')  # {1, 3, 7, 9}

#
s6 = s1.union(s2)
print(f'set6: {s6}')  # {1, 3, 5, 7, 9}
s6 = s1 | s2
print(f'set6: {s6}')  # {1, 3, 5, 7, 9}