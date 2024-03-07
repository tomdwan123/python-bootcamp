# opening and reading files

# rt: read text file
# rb: read binary file

print("#" * 5, "opening and reading files")
f = open("configuration.txt", "rt")
content = f.read()
print(content)
print(f.closed)
f.close()
print(f.closed)

# absolute and relative paths
# open("\\Users\\phucle\\Desktop\\Aduro\\Personal\\python\\python-bootcamp\\configuration.txt")
# open(r"\Users\phucle\Desktop\Aduro\Personal\python\python-bootcamp\configuration.txt")
open("/Users/phucle/Desktop/Aduro/Personal/python/python-bootcamp/configuration.txt")

# . => current working directory
# .. => parent directory

# reading files
print("#" * 5, "reading files")
f = open("configuration.txt", "rt")
content = f.read(5) # read 5 first letters
print(content)

print(f.tell()) # check position cursor
print(f.seek(2)) # move cursor
content = f.read(5)
print(content)

# with statement
print("#" * 5, "with statement")
with open("configuration.txt") as file:
    content = file.read()
    print(content)

print(file.closed)

# reading files into a list
print("#" * 5, "reading files into a list")
with open("configuration.txt") as file:
    content = file.read().splitlines()
    print(content)

with open("configuration.txt") as file:
    content = file.readlines()
    print(content)

with open("configuration.txt") as file:
    content = list(file)
    print(content)

with open("configuration.txt") as file:
    for line in file:
        print(line, end='')

# writing to text files
print("#" * 5, "writing to text files")
with open("writefile.txt", 'w') as file: # create file if not exist and override content
    file.write("First line\n")

with open("writefile.txt", 'a') as file: # create file if not exist and not override content
    file.write("Line with a\n")

with open("writefile.txt", 'r+') as file:
    file.write("Line with r+\n")
