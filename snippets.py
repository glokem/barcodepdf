# pulls a list of numbers from external text file and puts them into a list
fname = open('code_list.txt', 'r')
line = fname.readline()
codes = []
while (len(line) != 0):
	line_int=int(line) # cast each line as an int
	codes.append(line_int)
	line=fname.readline()
fname.close()


# loop this inside barcode placement to pull strings to generate barcodes
string = str(codes.pop())


# take used barcodes, put them in a seperate list to prevent future duplications
x=open('code_list.txt', 'w')
for number in codes:
	x.write('%d\n' % number)
x.close()	


import random

# some code to generate an independant list code barcodes
codes = []
i=0
while i < 6000:
	f=open('test_list.txt', 'r')
	line = f.readline()

	while (len(line) != 0):
		line_float=float(line)
		codes.append(line_float)
		line=f.readline()
	f.close()

	number = random.randrange(1000000,9999999)
	if number not in codes:
		f=open('test_list.txt', 'a')
		f.write('%d\n' % number)
		f.close()
	i = i + 1
