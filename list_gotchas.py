l1 = [1, 2, 3]
l2 = l1
l3 = l1.copy();
l1[0] = "XXX"
l1.append(4)
print(id(l1), id(l2), id(l3))