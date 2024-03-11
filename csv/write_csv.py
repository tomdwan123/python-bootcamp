import csv
with open("people.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (1, "John", "Amsterdam")
    writer.writerow(csvdata)