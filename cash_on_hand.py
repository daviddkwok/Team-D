from pathlib import Path
import csv
from api import forex

def coh_function(forex):
    """
    Cash on hand function with the variable forex
    function opens the cash on hand csv file to read
    appends the dates and cash on hand on two empty lists
    checks if there is a cash deficit between the days
    (if any) calculates the cash deficit 
    and appends to the summary report
    """

    # assigning the file path of cash on hand csv file to coh_fp
    coh_fp = Path.cwd()/'csv_reports'/'cash-on-hand-usd.csv'

    # assigning the file path of summary report file to summary_path
    summary_path = Path.cwd()/'summary_report.txt'

    # creating two empty lists for day list and amount list
    day_list = []    
    amount_list = []

    # opening cash on hand csv file to read with a variable 'file'
    with coh_fp.open(mode = 'r',encoding = 'UTF-8', newline = "") as file:

        # assign csv.reader() object to reader to read the csv file
        reader = csv.reader(file)

        # next() to skip the header
        next(reader)

        # create for loop for line in reader
        for line in reader:

            # adds on the days to the day empty list
            day_list.append(float(line[0]))

            # adds on the float cash on hand amount to the amount empty list
            amount_list.append(float(line[1]))

        # creating an empty variable, index
        index = 0
        
        # creating an empty variable, cash_deficit
        cash_deficit = 0

        # using while loop to run through all the days in the day list
        while index + 1 < len(day_list):

            # if function to check if the earlier float cash on hand amount is larger than the following day
            if float(amount_list[index]) > float(amount_list[index + 1]):

                # calculates the difference between the earlier amount and the following day amount and assigns to the empty variable 'cash_deficit'
                cash_deficit = (amount_list[index]) - (amount_list[index + 1])

                # converts the cash_deficit from usd to sgd by multiplying using the forex variable
                sgd_cash_deficit = cash_deficit * forex

                # opening the summary report to append with a variable 'file' 
                with summary_path.open(mode = 'a', encoding = 'UTF-8', newline = "") as file:

                    # to append multiple lines of f strings onto the file 
                    # and iterate over the day list and sgd cash deficit (1 dp) using writelines()
                    file.writelines(f'\n[CASH DEFICIT] DAY: {day_list[index + 1]}, AMOUNT: SGD{round(sgd_cash_deficit,1)}')

            # adds 1 to the index every time it loops
            index = index + 1

        # if function to check if cash_deficit still have a value of 0
        if cash_deficit == 0:

            # opening summary report to append with a variable 'file' 
            with summary_path.open(mode = 'a', encoding= 'UTF-8', newline= "") as file:

                # appends the message of cash surplus onto the summary report if there is no cash deficit
                file.write('\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

# recalls the cash on hand function 
coh_function(forex)