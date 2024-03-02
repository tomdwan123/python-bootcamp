# print() len() min() max() round() type() sum() upper() lower()

print(dir(str))
help(str.replace)

message = "I learn Python Programming"

# upper()
print(message.upper())

# lower()
print(message.lower())

# strip()
ip = '  192. 0. 0.1'
ip = ip.strip() # 192. 0. 0.1
print(ip)

dollar = "$$200$$"
print(dollar.strip("$")) # 200

# replace()
euro = dollar.replace("$", "€")
print(euro)

# count()
txt = "I love Java, Java is cool"
print(txt.count("Java"))

# split()
print(txt.split())
print("10.3.4.5".split("."))

# join()
str_txt = "-".join(txt.split())
print(str_txt)

# find()
my_str = "I learn Python"
print(my_str.find("Python"))

# in
print("Golang" in my_str)

# not in
print("Golang" not in my_str)

# capitalize()
s = 'pYThoN'
print(s.capitalize()) # Python
