from pathlib import Path
import csv


profit_lossfp = Path.cwd()/'csv_reports'/'profit-and-loss-usd.csv'
summary_path = Path.cwd()/'summary_report.txt'


# def cohfunction(forex):

day_list = []    
pl_list = []

with profit_lossfp.open(mode='r',encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            day_list.append(float(line[0]))
            pl_list.append(float(line[4]))
        index = 0
        pl_deflict = 0 
        while index+1<len(pl_list):
            if float(pl_list[index])>float(pl_list[index+1]):
                pl_deflict = float(pl_list[index])- float(pl_list[index+1])

                with summary_path.open(mode='w', encoding='UTF-8') as file:
                    file.writelines(f'\n[PROFIT DEFICIT] DAY: {day_list[index+1]}, AMOUNT: SGD{pl_deflict}')
            index = index+1
            file.close()
        if pl_deflict == 0:
            with summary_path.open(mode='w',encoding='UTF-8') as file:
                file.writelines('\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
        file.close()