from pathlib import Path
import csv
from api import forex

# assigning the file path of overheads csv to fp
overhead_fp = Path.cwd()/'csv_reports'/'overheads-day-40.csv'
summary_path = Path.cwd()/'summary_report.txt'

# creating two empty lists for empty list and overhead
empty_list = []
overhead_list = []

def overhead_function():
    # opening csv file to read with a variable 'file'
    with overhead_fp.open(mode='r',encoding='UTF-8', newline='') as file:
    
        #assign .reader() object to reader to read file
        reader = csv.reader(file)

        # next() to skip the header
        next(reader)

        # create for loop for line in text 
        for line in reader:

            # adds on the overhead categories to the overhead empty list
            overhead_list.append(line[0])

            # adds on the float overhead amounts to the empty_list
            empty_list.append(float(line[1]))

    # using the max() function to find the maximum value in the empty list and assigns to variable, max_amount
    global max_amount
    max_amount = max(empty_list)
    
    # finding the index position of the max_amount value and assigns to variable, index 
    index = empty_list.index(max_amount)

    # locates the position of the category by using the index position from the overhead list
    category = (overhead_list[index])

    # converts the category to all uppercase
    global upper_overheads
    upper_overheads = category.upper()

    # stores a message for highest overheads category and amount using f-strings
    message = f'[HIGHEST OVERHEADS] {upper_overheads}: SGD{(max_amount)}'

    # shows the message
    print(message)

    # with summary_path(mode="w", encoding = 'UTF-8', newline = "") as file:
    #     writer=csv.writer(file)
    #     writer.writerows('hello')

overhead_function()


# with summary_path(mode="w", encoding = 'UTF-8', newline = "") as file:
#     writer=csv.writer(file)
#     writer.writerows('hello')