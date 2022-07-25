from pathlib import Path

fp = Path.cwd()/'csv_reports'/'profit-and-loss-thb.csv'
print(fp.exists())