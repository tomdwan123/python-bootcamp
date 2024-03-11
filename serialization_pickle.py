import pickle
friend1s = {"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 43525222]}
friend2s = {"Andrei": [30, "NYC", 3234342], "Tony": [25, "Madrid", 43525222]}
friends = (friend1s, friend2s)

with open("friends.dat", "wb") as f:
    pickle.dump(friends, f, )

with open("friends.dat", "rb") as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)