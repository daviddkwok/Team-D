import api, cash_on_hand, overheads, profit_loss
from pathlib import Path
from api import forex

# assigning the file path of summary report file to summary_path
summary_path = Path.cwd()/'summary_report.txt'

# creates a new file with .touch()
summary_path.touch()

def main():
    api.api_function()
    overheads.overhead_function(forex)
    cash_on_hand.coh_function(forex)
    profit_loss.profitloss_function(forex)
main()