from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'overheads-day-40.csv'
print(fp.exists())
empty_list = []
with fp.open(mode='r',encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        empty_list.append(line[1])
print(empty_list)


max_number = (empty_list.sort(reverse=True))
print(max_number)

print(empty_list)
print(type(float(max(empty_list))))
# for data in text:

# print(text)
