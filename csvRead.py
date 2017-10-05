import csv

with open('symbolsAll.csv', 'rU') as csv_file:
	# Python 2.5 incorporated "with." 
	# It has special methods to ensure 
	# a file is (properly and safely)
	# opened and closed 
	# (to prevent file corruption)
	# (to free up memory)
	# even if an exception occurs.

#csv_file = open('symbolsAll.csv', 'rU')

	data = csv_file.read()

	for row in data:
		print(row)

	csv_file.close()

# This worked,but it produces
# one character per line in the print

