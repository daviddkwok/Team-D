from pathlib import Path
import csv
from api import forex

def overhead_function(forex):
    """
    Overhead function opens the overhead csv file to read
    finds the max value in the overhead csv file
    and appends to the summary report
    """

    # assigning the file path of the overheads csv file to overhead_fp
    overhead_fp = Path.cwd()/'csv_reports'/'overheads-day-40.csv'

    # assigning the file path of summary report file to summary_path
    summary_path = Path.cwd()/'summary_report.txt'

    # creating two empty lists for amount list and overhead list
    amount_list = []
    overhead_list = []
    
    # opening overhead csv file to read with a variable 'file'
    with overhead_fp.open(mode = 'r', encoding = 'UTF-8', newline = "") as file:
    
        # assign .reader() object to reader to read file
        reader = csv.reader(file)

        # next() to skip the header
        next(reader)

        # create for loop for line in reader
        for line in reader:

            # adds on the overhead categories to the overhead empty list
            overhead_list.append(line[0])

            # adds on the float overhead amounts to the empty_list
            amount_list.append(float(line[1]))

    # using the max() function to find the maximum value in the empty list and assigns to variable, max_amount
    max_amount = max(amount_list)

    # converts the max_amount from usd to sgd by multiplying using the forex variable and assigns to sgd_max_amount
    sgd_max_amount = max_amount * forex

    # finding the index position of the max_amount value and assigns to variable, index 
    index = amount_list.index(max_amount)

    # locates the position of the category by using the index position from the overhead list
    category = (overhead_list[index])

    # converts all the letters in 'category' to uppercase
    upper_overheads = category.upper()

    # opening the summary report to append with a variable 'file' 
    with summary_path.open(mode = 'a', encoding = 'UTF-8', newline = "") as file:

        # append the highest overhead category and sgd amount onto the summary report
        file.write(f"\n[HIGHEST OVERHEADS] {upper_overheads}: SGD{(sgd_max_amount)}")

# recalls the overhead function 
overhead_function(forex)