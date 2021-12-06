from filereader import *

if __name__ == '__main__':
	# file = as_int(read_comma_sep("test"))
	file = as_int(read_comma_sep("day06"))

	counter = [0]*9

	for x in file:
		counter[x] += 1


	for x in range(256):
		new_counter = [0]*9
		for i, x in enumerate(counter):
			if i == 0:
				new_counter[8] += x
				new_counter[6] += x
			else:
				new_counter[i-1] += x
		counter = new_counter
	print(sum(counter), counter)