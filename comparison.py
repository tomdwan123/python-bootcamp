# ==
print(7 == 8) # False
print('a' == 'a') # True

# !=
print(7 != 7) # False
print('a' != 'A') # True

# >
print(7 > 9) # False

# =
print(7 >= 7) # True

# <
print(7 < 4) # False

# <=
print(7 <= 9) # True

# is
a, b = 3, 4
print(a is b)

# is not
print(a is not b)

# append()
l = [1, 2, 3]
print(id(l))
l.append(4)
print(id(l)) # list immutable

# copy()
li = l.copy()
print(id(li))
print(l == li) # compare value
print(l is li) # compare address