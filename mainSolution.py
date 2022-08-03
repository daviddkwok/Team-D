import api, cash_on_hand, overheads, profit_loss
from pathlib import Path
from api import forex

summary_path = Path.cwd()/'summary_report.txt'
summary_path.touch()
def main():
    api.api_function()
    overheads.overhead_function(forex)
    cash_on_hand.coh_function(forex)
    profit_loss.profitloss_function(forex)
main()