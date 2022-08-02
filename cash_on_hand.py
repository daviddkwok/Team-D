from pathlib import Path
import csv

coh_fp = Path.cwd()/'csv_reports'/'cash-on-hand-usd.csv'
summary_path = Path.cwd()/'summary_report.txt'
summary_path.touch()

# def cohfunction(forex):

day_list = []    
amount_list = []

with coh_fp.open(mode='r',encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            amount_list.append(float(line[1]))
            day_list.append(float(line[0]))
        index = 0
        cash_deflict = 0 
        while index+1<len(amount_list):
            if float(amount_list[index])>float(amount_list[index+1]):
                cash_deflict = float(amount_list[index])- float(amount_list[index+1])

                with summary_path.open(mode='w', encoding='UTF-8', newline = '') as file:
                    writer=csv.writer(file)
                    writer.writelines(f'\n[CASH DEFICIT] DAY: {day_list[index+1]}, AMOUNT: SGD{cash_deflict}')
            index = index+1
            # file.close()
        if cash_deflict == 0:
            with summary_path.open(mode='a',encoding='UTF-8') as file:
                file.writelines('\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
                # file.close()
        file.close()

# print(cohfunction(forex))
