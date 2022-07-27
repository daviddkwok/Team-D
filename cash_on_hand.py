from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'cash-on-hand-usd.csv'
print(fp.exists())

with fp.open(mode='r',encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        print(line[1])
        