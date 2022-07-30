from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'overheads-day-40.csv'

empty_list = []
overhead = []
with fp.open(mode='r',encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        empty_list.append(float(line[1]))
        overhead.append(line[0])
max_amount = max(empty_list)
index = empty_list.index(max_amount)
overheads = (overhead[index])
upper_overheads = overheads.upper()

message = f'[HIGHEST OVERHEADS] {upper_overheads}: SGD{max_amount}'
print(message)