# Ryan Lauderback
# Fall 2017
# This is the code for the first question of the Capital one project, I am finding the average prices of neighborhood airbnb
# This code is finding the sum and average of the data from the csv file.

import sys
import csv

nextval = sys.stdin.readline()

price = 0.0
daysBooked = 0
averageWeeklyEarnings = 0.0
totalEarnings = 0.0
nameCurrent = "0000000"
averagePrices = []

nextval = sys.stdin.readline() 
values = nextval.split(',')
	# while nextval.strip() != '':
price = float(values[0])
print price
daysBooked = float(values[1])
print daysBooked
totalEarnings = price * daysBooked
averageWeeklyEarnings = totalEarnings / 52
averagePrices.append(averageWeeklyEarnings)

while nextval.strip() != '':
	values = nextval.split(',')
	print values
	price = float(values[0])
	daysBooked = float(values[1])
	totalEarnings = price * daysBooked
	averageWeeklyEarnings = totalEarnings / 52
	averagePrices.append(averageWeeklyEarnings)
	# move to next line
	nextval = sys.stdin.readline() 
print averagePrices

download_dir = "listingAverageWeeklyEarning.csv"
# csv = file(download_dir, "w")
columnTitleRow = "Average Weekly Earning"

	
with open(download_dir, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow([columnTitleRow])
    for val in averagePrices:
        writer.writerow([val])

