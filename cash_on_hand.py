from pathlib import Path
import csv
from api import forex

def coh_function():
    """
    Function opens the cash on hand csv file 
    checks if there is a cash deficit between the days
    and appends to the summary report
    """

    # assigning the file path of cash on hand csv to coh_fp
    coh_fp = Path.cwd()/'csv_reports'/'cash-on-hand-usd.csv'
    # assigning the file path of summary report to summary_path
    summary_path = Path.cwd()/'summary_report.txt'

    # creating two empty lists for day list and amount list
    day_list = []    
    amount_list = []

    # opening cash on hand csv file to read with a variable 'file'
    with coh_fp.open(mode='r',encoding='UTF-8', newline='') as file:

        # assign .reader() object to reader to read file
        reader = csv.reader(file)

        # next() to skip the header
        next(reader)

        # create for loop for line in reader
        for line in reader:

            # adds on the float days to the day empty list
            day_list.append(float(line[0]))

            # adds on the float cash on hand amount to the amount empty list
            amount_list.append(float(line[1]))

        # assigns 0 to a variable, index
        index = 0

        # assigns 0 to a variable, cash deficit
        cash_deficit = 0 

        
        while index+1<len(amount_list):
            if float(amount_list[index])>float(amount_list[index+1]):
                cash_deficit = (amount_list[index])- (amount_list[index+1])
                with summary_path.open(mode='a', encoding='UTF-8', newline = '') as file:
                    file.writelines(f'\n[CASH DEFICIT] DAY: {day_list[index+1]}, AMOUNT: SGD{cash_deficit}')
            index = index+1

        if cash_deficit == 0:
            with summary_path.open(mode='a',encoding='UTF-8') as file:
                file.writelines('\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

coh_function()
