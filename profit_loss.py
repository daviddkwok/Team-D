from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'profit-and-loss-usd.csv'
print(fp.exists())
empty_list = []
with fp.open(mode='r',encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        empty_list.append(line[4])



print(empty_list)        
print(empty_list[1])
