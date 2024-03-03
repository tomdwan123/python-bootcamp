l1 = [1, 2, 3]
l2 = l1
l3 = l1.copy();
l1[0] = "XXX"
l1.append(4)
print(id(l1), id(l2), id(l3))

l1 = list('ab')
l2 = l1
l1.append('c')
print(l2)
print(l1)

# sorted() and list.sort()
l1 = [2, 3, 1, 5, 4]
la = sorted(l1)
print(la, l1)

lb = l1.sort()
print(lb, l1)

l1.sort(reverse=True)
print(l1)

years = [2022, 2020, 2021]
print(years.sort())

friends = ["Tony", "paul", "Ancb"]
my_friends = [item.capitalize() for item in friends]
print(my_friends)

reversed_names = [item[::-1] for item in friends]
print(reversed_names)

nums = [1, 7, 9, 14, 15, 21, 25]
disivible_by_seven = [num for num in nums if num % 7 == 0]
print(disivible_by_seven)

num_str = [str(n) for n in nums]
print(num_str)
print("-".join(num_str))