for _ in range(10):
    print("Do some thing", _)

import random
names = ["A", "B", "C", "D", "E", "F"]
for _ in names:
    print(f'Choosing winner. Round {_}')
    winner = random.choice(names)
    names.remove(winner)
    print(winner)
    print("######")