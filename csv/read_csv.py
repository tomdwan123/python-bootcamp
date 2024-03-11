import csv

with open("airtravel.csv", "r") as f:
    rows = csv.reader(f)
    next(rows)   # ignore header row
    year_1985 = dict()
    for row in rows:
        year_1985[row[0]] = row[1]

    print(year_1985)

    max_1958 = max(year_1985.values())

    print(max_1958)

    for k, v in year_1985.items():
        if max_1958 == v:
            print(f'Busiest Month in 1958: {k}, Flights: {v}')