path = "google_stock_data.csv"
lines = [line for line in open(path)]

print lines[0]
print lines[1]

# strip() method to remove any leading or trailing whitespace
print lines[0].strip()

# split() method to divide the string into smaller pieces
print lines[0].strip().split(',')

dataset  = [line.strip().split(',') for line in open(path)]

print dataset[1] # still data are sting

# if the dataset is containing movies name or books name, 
# so there will be many names with comma, then it will split those names also
# spliting on comma it will split those names too 
# we should use csv module to overcome these problems