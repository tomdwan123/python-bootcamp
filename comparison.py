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

# format()
print(format(1/3, '.5f')) # 0.33333

a = 0.1 * 3
b = 0.3
print(format(a, '.25f'))
print(format(b, '.25f'))
print(a == b) # False

from math import isclose
x = 0.0000000001
y = 0.0000000002
print(x == y) # False
print(isclose(x, y, abs_tol=0.01)) # True

a = 999999999.01
b = 999999999.02
print(a == b) # False
print(isclose(a, b, rel_tol=0.01)) # True

a = 3.4
b = 2.3
print(format(a, '.25f'))
print(format(b, '.25f'))
print(a + b) # is not 5.7