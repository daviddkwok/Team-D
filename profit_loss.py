from pathlib import Path
import csv

fp = Path.cwd()/'csv_reports'/'profit-and-loss-usd.csv'

empty_list = []
day_list = []
position = 0
with fp.open(mode='r',encoding='UTF-8', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        day_list.append(float(line[0]))
        empty_list.append(float(line[4]))
        # if empty_list[0] > empty_list[1]:
        #     print(day_list)
    if empty_list[position]>empty_list[position+1]:
        print(day_list)
        
#     print(empty_list[1])
# print(day_list)
# print(empty_list)
# print(empty_list[1])

