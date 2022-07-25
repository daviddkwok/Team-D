from pathlib import Path

fp = Path.cwd()/'csv_reports'/'overheads-day-45.csv'
print(fp.exists())