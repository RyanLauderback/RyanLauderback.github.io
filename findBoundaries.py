# Ryan Lauderback
# Fall 2017
# This is the code for the first question of the Capital one project, I am finding the average prices of neighborhood airbnb
# This code is finding the sum and average of the data from the csv file.

# task 2, adding 

# take in longitude and latitutude to determine the bondaries of the grid

import sys
import math 


latMax = 0.0
latMin = 200.0
longMin = -1.0
longMax = 0.0
nameCurrent = "0000000"


nextval = sys.stdin.readline() 
nextval = sys.stdin.readline()
values = nextval.split(',')
latMin = values[0]
longMin = values[1]
print latMin
print longMin
nextval = sys.stdin.readline()

while nextval.strip() != '':
	values = nextval.split(',')
	lat = values[0]
	longt = values[1]

	# print lat, " ", longt
	# print latMin
	# print longMin
	if lat > latMax:
		latMax = lat

	if latMin > values[0]:
		latMin = values[0]
		print latMin
	else:
		latMin = latMin

	if longt > longMax:
		longMax = longt
	if longt < longMin: 
		longMin = longt
		print longMin
	
	nextval = sys.stdin.readline() 
print latMin

boundaries = [latMax, latMin, longMax, longMin]
# LatMax 37.83109279
# LatMin 37.70692769

# LongMax -122.5115
# LongMin -122.3647585
print boundaries