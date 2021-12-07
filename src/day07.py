from filereader import *
from helper import Memoize


@Memoize
def calc_costs(x):
	sum = 0
	for i in range(x+1):
		sum += i
	return sum

if __name__ == '__main__':
	# file = as_int(read_comma_sep("test"))
	file = as_int(read_comma_sep("day07"))

	cheapest = 99999999999

	cheap_array = []

	for i in range(max(file)):
		cheap_check = 0
		cheaper = True
		for j in range(len(file)):
			cheap_check += calc_costs(abs(i - file[j]))
			if cheap_check > cheapest:
				cheaper = False
				break
		cheap_array.append(cheap_check)
		if cheaper:
			cheapest = cheap_check

	print(cheap_array)
	print(cheapest)