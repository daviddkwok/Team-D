from pathlib import Path

fp = Path.cwd()/'csv_reports'/'cash-on-hand-thb.csv'
print(fp.exists())