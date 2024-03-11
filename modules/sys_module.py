import sys

print(f'Number of arguments: {len(sys.argv)}')
print(f'This is name of the script: {sys.argv[0]}')
print(f'The script arguments are: {sys.argv}')

## Redirecting output to a file instead of stdout (console)
original_stdout = sys.stdout    # saving the original stdout

## Using a file as stdout, redirecting output to a file
with open("stdout.txt", "w") as sys.stdout:
    print("Printing a string")
    x = 10
    print(f'x is {x}')

sys.stdout = original_stdout