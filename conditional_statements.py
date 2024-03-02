
balance = 100
price = 50

if balance >= price:
    new_balance = balance = price
    print(f"You can book flight and your new balance is {new_balance}")
else:
    print(f"Insufficient funds! Please deposit {price - balance}")

answer = input("Do you want to continue: yes or no: ")
if answer == "yes":
    print("We will go on")
elif answer == "no":
    print("We will stop")
else:
    print("Invalid answer")