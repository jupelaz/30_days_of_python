"""Day 16: 30 Days of python programming"""
from datetime import datetime
# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
now.day
print(f'{now.day} {now.month} {now.year} {now.minute} {now}')
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
# Today is 5 December, 2019. Change this time string to time.
dec_5 = datetime.strptime("5 December, 2019", "%d %B, %Y")
print(dec_5)
# Calculate the time difference between now and new year.
new_year = datetime(2024, 1, 1)
diff = new_year - now
print(diff)
# Calculate the time difference between 1 January 1970 and now.
print(datetime(1970, 1, 1) -now)
