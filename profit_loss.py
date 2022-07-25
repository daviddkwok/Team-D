from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'profit-and-loss-thb.csv'
print(fp.exists())

with fp.open(mode='r',encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        print(line[4])