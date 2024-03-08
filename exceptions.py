# case 1
while True:
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = a / b
    except ZeroDivisionError as e:
        print("An exception has occured")
    else:
        print("No error")
        print(f'c={c}')
        break
    finally:
        print("Goodbye")

    x = 10
    print(x**x)
    print("some other code")

# case 2
f = open('a.txt', 'w')
try:
    f.write("write something to the file")
except:
    print("Cannot write to file")
else:
    print('"File was written successfully')
finally:
    print("This code is always executed")
    if not f.closed:
        f.close()
    print(f'File closed: {f.closed}')

print("some other code ...")

# case 3
age = -1
if age < 0:
    raise Exception("Age below zero is not permitted")