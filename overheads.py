from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'overheads-day-40.csv'
print(fp.exists())
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
print(max_amount)
highestoverhead = (overhead[index])
uppercase = highestoverhead.upper()

message = f'[HIGHEST OVERHEADS] {uppercase}: SGD{max_amount}'
print(message)