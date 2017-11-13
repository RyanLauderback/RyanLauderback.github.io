# Ryan Lauderback
# Fall 2017
# This is the code for the first question of the Capital one project, I am finding the average prices of neighborhood airbnb
# This code is finding the sum and average of the data from the csv file.

import sys
import csv

nextval = sys.stdin.readline()
sum = 0.0
count = 0 
nameID = "00000000"
nameCurrent = "0000000"
availability = []
availabilityCSV = []
nextval = sys.stdin.readline() 
words = nextval.split(',')
	# while nextval.strip() != '':
nameCurrent = words[0]
nameID = nameCurrent
while nextval.strip() != '':
	words = nextval.split(',')
	# print words[2] , " ", words[0]
	nameCurrent = words[0] 
	if nameCurrent == nameID:
		if words[2] == 'f':
			count += 1

	if words[0] != nameID:
		nameID = nameCurrent
		availability.append(count)
		count = 0 
		if words[2] == 'f':
			count += 1
	nextval = sys.stdin.readline() 
# print "nights available of each property: ", availability
# print "length of list: ", len(availability)
print availability
# Writing of csv file listing availability 
download_dir = "listingAvailability.csv"
# csv = file(download_dir, "w")
columnTitleRow = "pastBooking"

	
with open(download_dir, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow([columnTitleRow])
    for val in availability:
        writer.writerow([val])



