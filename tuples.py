t1 = (10,)
print(type(t1))

t2 = 10, "a", True, 2.5
print(type(t2))

t3 = tuple([1, 2, 3, 4])
t4 = tuple("hello")
print(type(t3), type(t4))

print(list(t2))

my_tuple = (10, True, 2.5, (30, 4), "x")
t1 = my_tuple + tuple("y")
print(t1)

# TUPLES and LISTS

# 1. Tuples are faster and more efficient than lists

# 2. Tuples are safer than lists

# 3. Tuples are used as keys in dictionaries

# 4. Storage effi
import sys;

l1 = [1, 2, 3, 4, 5, 6, 7]
t1 = (1, 2, 3, 4, 5, 6, 7)
print(sys.getsizeof(l1)) # 120
print(sys.getsizeof(t1)) # 96