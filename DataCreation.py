# Ryan Lauderback
# Fall 2017
# Capital One SanFran AirBnb Optimizer

#This program creates the data set that the JS will access 

import sys 
import math
from operator import itemgetter

dataString = ""
locationPointsWE = []
locationPointsNS = []
iterations = 10

LatMax = 37.83109279
LatMin = 37.70692769
latSize = LatMax - LatMin

longMax = -122.5115
LongMin = -122.3647585
LongSize = LongMin - longMax
print latSize, LongSize

# Creates data grid of latitudes and longitudes

for x in range(0, 10):
	locationPointsNS.append((float(x) * (latSize/10.0)) + LatMin)
	locationPointsWE.append((float(x) * (LongSize/10.0)) + longMax)
print locationPointsNS
print locationPointsWE


# assigns values to the grid points by pulling the data set information
# Grabbing Data
dataSet = []
nextval = sys.stdin.readline() 
nextval = sys.stdin.readline() 
while nextval.strip() != '':
	values = nextval.split(',')
	
	dataSet.append(values)
	# move to next line
	nextval = sys.stdin.readline() 
dataSet = dataSet[:-1]

# Loops for the grid and then assigns 
gridData = []
distanceGridPoint = 0.0
distanceMin = 1.0
orderedDataSet = []
orderedDataSetTop50 = []
orderedDataSetTop25 = []
average = 0.0
averagePrice = 0.0
averageEarnings = 0.0
for x in locationPointsNS:
	for y in locationPointsWE:
		gridData = []
		distanceGridPoint = 0.0
		distanceMin = 1.0
		orderedDataSet = []
		orderedDataSetTop50 = []
		orderedDataSetTop25 = []
		earningsTotal = 0.0
		averagePrice = 0.0
		averageEarnings = 0.0
		gridData.append(locationPointsNS[locationPointsNS.index(x)])
		gridData.append(locationPointsWE[locationPointsWE.index(y)])
		print gridData
		# looping through listings to find 50 closest
		for airBnb in dataSet:
			distanceGridPoint = math.sqrt((float(gridData[0]) - float(airBnb[0]))**2 + (float(gridData[1]) - float(airBnb[1]))**2)
			airBnb.append(distanceGridPoint)
			
			# print distanceGridPoint
			orderedDataSet.append(airBnb)
		# orders the pairs and keeps top 50
		# sorted(orderedDataSet,key=itemgetter(6))

		orderedDataSet.sort(key=lambda x: x[6], reverse = True)
		orderedDataSetTop50 = orderedDataSet[:50]
		for value in orderedDataSetTop50:
			earningsTotal += float(value[5])
			# averagePrice += float(value[3])
			# print value[5], value[3]
		averageEarnings = earningsTotal / 50.0
		# averagePrice = averagePrice / 50.0


		# sorts list based on highest number of bookings
		orderedDataSetTop50.sort(key=lambda x: x[4], reverse = True)
		orderedDataSetTop25 = orderedDataSetTop50[:25]
		# print orderedDataSetTop50
		for value in orderedDataSetTop25:
			averagePrice += float(value[3])
		
		averagePrice = averagePrice / 25.0

		data0 = str(gridData[0])
		data1 = str(gridData[1])
		dataString += data0 + "," + data1 + "," + str(averageEarnings) + "," + str(averagePrice) + "; "
		for airBnb in dataSet:
			del airBnb[-1]

print dataString











