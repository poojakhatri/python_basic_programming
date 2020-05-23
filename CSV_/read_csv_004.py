# importing csv module

import csv
from datetime import datetime
path = "google_stock_data.csv"
file = open(path)
reader = csv.reader(file)
  
header =  next(reader) # The first line is the header

data = []
for row in reader:
	# ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close']
	date  = datetime.strptime(row[0], '%m/%d/%Y' )
	open_price = float(row[1])
	high = float(row[2])
	low = float(row[3])
	close = float(row[4])
	volume = float(row[5])
	adj_close = float(row[6])

	data.append([date, open_price, high, low, close, volume, adj_close])

#print data[0]
# Compute and store daily stock returns
returns_path ="google_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
	todays_row = data[i]
	todays_date = todays_row[0]
	todays_price = todays_row[-1]
	yesterday_row = data[i+1]
	yesterday_price = yesterday_row[-1]

	daily_return  = (todays_price - yesterday_price)/ yesterday_price
	formatted_date = todays_date.strftime('%m/%d/%Y')
	writer.writerow([formatted_date, daily_return])

