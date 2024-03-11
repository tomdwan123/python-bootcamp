import csv
with open("items.csv", "r") as f:
    reader = csv.reader(f, delimiter="#", lineterminator="\n")
    next(reader)
    for row in reader:
        print(row)