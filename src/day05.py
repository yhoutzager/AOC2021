from filereader import *

if __name__ == '__main__':
	# file = read_lines("test")
	file = read_lines("day05")

	line_list = [[[int(z) for z in y.split(",")] for y in x.split(" -> ")] for x in file]
	max_x = max([y[0] for x in line_list for y in x])
	max_y = max([y[1] for x in line_list for y in x])

	roster = [[0]*(max_x + 1) for i in range(max_y + 1)]
	for co_1, co_2 in line_list:
		if (co_1[0] == co_2[0] or co_1[1] == co_2[1]):
			min_x = min(co_1[0], co_2[0])
			max_x = max(co_1[0], co_2[0])
			min_y = min(co_1[1], co_2[1])
			max_y = max(co_1[1], co_2[1])

			for x in range(min_x, max_x + 1):
				for y in range(min_y, max_y + 1):
					roster[y][x] += 1
			continue
		else:
			if co_1[0] < co_2[0]:
				mi = co_1
				ma = co_2
			else:
				mi = co_2
				ma = co_1
			if mi[1] > ma[1]:
				for x in range(0, ma[0] - mi[0] + 1):
					roster[mi[1] - x][mi[0] + x] += 1
			else:
				for x in range(ma[0] - mi[0], -1, -1):
					roster[mi[1] + x][mi[0] + x] += 1



	# [print(x) for x in roster]

	count = len([y for x in roster for y in x if y > 1])
	print(count)
