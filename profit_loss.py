from pathlib import Path
import csv
from api import forex

def profitloss_function(forex):
    """
    Profit loss function with the variable forex
    function opens the profit and loss csv file
    appends the date and profit/loss on two empty lists
    checks if there is a net profit deficit between the days
    (if any) calculates the pl deficit 
    and appends to the summary report
    """

    # assigning the file path of profit and loss csv file to profit_lossfp
    profit_lossfp = Path.cwd()/'csv_reports'/'profit-and-loss-usd.csv'

    # assigning the file path of summary report file to summary_path
    summary_path = Path.cwd()/'summary_report.txt'

    # creates two empty lists for day list and pl list
    day_list = []    
    pl_list = []

    # opening profit loss csv file to read with a variable 'file'
    with profit_lossfp.open(mode = 'r',encoding = 'UTF-8', newline = "") as file:

        # assign csv.reader() object to reader to read the csv file
        reader = csv.reader(file)

        # next() to skip the header
        next(reader)

        # create for loop for line in reader
        for line in reader:

            # adds on the float days to the day empty list
            day_list.append(float(line[0]))

            # adds on the float profit and loss amount to the profit loss empty list
            pl_list.append(float(line[4]))

        # creating an empty variable, index
        index = 0

        # creating an empty variable, pl_deficit
        pl_deflict = 0 

        # using while loop to run through all the days in the day list
        while index + 1 < len(day_list):

            # if function to check if the earlier float p/l amount is larger than the following day
            if float(pl_list[index]) > float(pl_list[index + 1]):

                # calculates the difference between the earlier amount and the following day amount and assigns to a variable pl_deficit
                pl_deficit = float(pl_list[index]) - float(pl_list[index + 1])

                # converts the pl_deficit from usd to sgd by multiplying using the forex variable
                sgd_pl_deficit = pl_deficit * forex
                
                # opening the summary report to append with a variable 'file' 
                with summary_path.open(mode = 'a', encoding = 'UTF-8', newline = "") as file:

                    # to append multiple lines of the f string onto the file 
                    # and iterate over the day list and sgd pl deficit using writerows()
                    file.writelines(f'\n[PROFIT DEFICIT] DAY: {day_list[index + 1]}, AMOUNT: SGD{sgd_pl_deficit}')

            # adds 1 to the index every time it loops
            index = index + 1

        #  if function to check if pl_deficit is has a value of 0
        if pl_deflict == 0:

            # opening summary report to append with a variable 'file' 
            with summary_path.open(mode = 'a',encoding = 'UTF-8', newline = "") as file:

                # appends the message of net profit surplus onto the summary report if there is no net profit deficit
                file.write('\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

# recalls the profit loss function
profitloss_function(forex)