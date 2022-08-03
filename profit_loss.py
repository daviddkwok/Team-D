from pathlib import Path
import csv
from api import forex

def profitloss_function(forex):

    """
    Function appends the date and profit/loss on two empty lists
    Compares the profit/loss values to find if there is a deficit
    and appends to the summary report
    """

    # assigning the file path of profit and loss csv to profit_lossfp
    profit_lossfp = Path.cwd()/'csv_reports'/'profit-and-loss-usd.csv'

    # assigning the file path of summary report to summary_path
    summary_path = Path.cwd()/'summary_report.txt'

    # creates two empty lists for day list and pl list
    day_list = []    
    pl_list = []

    # opening profit loss csv file to read with a variable 'file'
    with profit_lossfp.open(mode='r',encoding='UTF-8', newline='') as file:

        # assign .reader() object to reader to read file
        reader = csv.reader(file)

        # next() to skip the header
        next(reader)

        # create for loop for line in reader
        for line in reader:

            # adds on the float days to the day empty list
            day_list.append(float(line[0]))

            # adds on the float profit and loss amount to the profit loss empty list
            pl_list.append(float(line[4]))

        # assigns 0 to a variable, index
        index = 0

        # assigns 0 to a variable, pl deficit
        pl_deflict = 0 

        # 
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