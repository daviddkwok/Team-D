from pathlib import Path
import csv


coh_fp = Path.cwd()/'csv_reports'/'cash-on-hand-usd.csv'

def cohfunction(forex):
    
    empty_list = []

    with coh_fp.open(mode='r',encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            empty_list.append(float(line[1]))
        index = 0
        deflict = 0 
        while index+1<len(empty_list):
            if float(empty_list[index])>float(empty_list[index+1]):
                deflict = float(empty_list[index])- float(empty_list[index+1])
        index = index+1
    # if deflict == 0:
    file.close()
    print(empty_list[0])


    print(empty_list)
