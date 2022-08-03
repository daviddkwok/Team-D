import api, cash_on_hand, overheads, profit_loss
from pathlib import Path
from api import forex

summary_path = Path.cwd()/'summary_report.txt'
summary_path.touch()
def main():
    forex = api.api_function()
    overheads.overhead_function()
    cash_on_hand.coh_function()
    profit_loss.profitloss_function()
main()