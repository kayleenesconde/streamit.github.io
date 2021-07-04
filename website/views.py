import csv

with open('tv_shows (1).csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for r in reader:
        print(r)

