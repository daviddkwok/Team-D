from pathlib import Path
import csv
from api import forex

def profitloss_function(forex):

    day_list = []    
    pl_list = []
    profit_lossfp = Path.cwd()/'csv_reports'/'profit-and-loss-usd.csv'
    summary_path = Path.cwd()/'summary_report.txt'
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
                pl_deficit = float(pl_list[index])- float(pl_list[index+1])
                with summary_path.open(mode='a', encoding='UTF-8') as file:
                    file.writelines(f'\n[PROFIT DEFICIT] DAY: {day_list[index+1]}, AMOUNT: SGD{pl_deficit*forex}')
            index = index+1

        if pl_deflict == 0:
            with summary_path.open(mode='a',encoding='UTF-8') as file:
                file.writelines('\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

profitloss_function(forex)