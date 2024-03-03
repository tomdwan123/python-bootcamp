import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
print(chars)
password = ''

len_password = int(input("Enter your length password: "))

for _ in range(len_password):
    char = random.choice(chars)
    password += char

print(f"Your random password is {password}")