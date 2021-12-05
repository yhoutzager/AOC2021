from filereader import *

if __name__ == '__main__':
	# file = read_lines("test")
	file = read_lines("day03")

	sum1 = [0] * len(file[0])

	for x in file:
		for i, dig in enumerate(x):
			sum1[i] += int(dig)

	gam, eps = "", ""
	cutoff = len(file) / 2
	for x in sum1:
		if x < cutoff:
			gam += "0"
			eps += "1"
		else:
			gam += "1"
			eps += "0"

	ans = int(gam, 2) * int(eps, 2)
	print(ans)

	filter_oxy = file.copy()
	filter_co2 = file.copy()
	sum0 = ""
	if sum1[0] < cutoff:
		sum0 = "0"
	else:
		sum0 = "1"
	filter_oxy = [x for x in filter_oxy if x[0] == sum0]
	filter_co2 = [x for x in filter_co2 if x[0] != sum0]
	oxy, co2 = 0, 0
	for i in range(1, len(file[0])):
		if len(filter_oxy) > 1:
			sum_oxy = sum([1 for x in filter_oxy if x[i] == '1'])

			res_oxy = ""
			if sum_oxy < len(filter_oxy) / 2:
				res_oxy = "0"
			else:
				res_oxy = "1"
			filter_oxy = [x for x in filter_oxy if x[i] == res_oxy]

		if len(filter_co2) > 1:
			sum_co2 = sum([1 for x in filter_co2 if x[i] == '1'])
			res_co2 = ""
			if sum_co2 < len(filter_co2) / 2:
				res_co2 = "1"
			else:
				res_co2 = "0"
			filter_co2 = [x for x in filter_co2 if x[i] == res_co2]

	ans2 = int(filter_oxy[0],2) * int(filter_co2[0],2)
	print(ans2)

	