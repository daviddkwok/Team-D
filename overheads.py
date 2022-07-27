from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'overheads-day-40.csv'
print(fp.exists())

with fp.open(mode='r',encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        print(line)

# for data in text:

# print(text)
