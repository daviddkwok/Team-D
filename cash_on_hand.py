from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'cash-on-hand-usd.csv'
print(fp.exists())
empty_list = []
pos = 0
with fp.open(mode='r',encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        empty_list.append(float(line[1]))

print(empty_list)
