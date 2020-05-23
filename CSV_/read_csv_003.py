# importing csv module

import csv

path = "google_stock_data.csv"
file = open(path)
reader = csv.reader(file)

header  = next(reader) # the first line in the header
data  = [row for row in reader] # read the remaining data

print header
print data[0] # still data is treated as string