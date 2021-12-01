from filereader import *

if __name__ == '__main__':
	# depths = as_int(read_lines("test"))
	depths = as_int(read_lines("day01"))
	counter = 0
	for x in range(1, len(depths)):
		if depths[x] > depths[x-1]:
			counter += 1

	print(counter)

	counter = 0
	for x in range(1, len(depths) - 2):
		a = depths[x-1] + depths[x] + depths[x+1]
		b = depths[x] + depths[x+1] + depths[x+2]
		if b > a:
			counter += 1

	print(counter)
