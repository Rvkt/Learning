import calendar
import os
from pathlib import Path

year = input('Enter Year: ')

if not os.path.exists(year):
    year_dir = Path(year)

for month_dir in range(1, 13):
    month = year_dir / f'{year_dir}_{str(month_dir).zfill(2)}'
    month.mkdir(parents=True)
