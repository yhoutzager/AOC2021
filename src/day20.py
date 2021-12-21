import time

from filereader import *


def get_bin(string):
	return int(string.replace(".", "0").replace("#", "1"), 2)


def build_string(_x, _y, _lit, _dark, default):
	string = ""
	for j in range(_y - 1, _y + 2):
		for i in range(_x - 1, _x + 2):
			if (i, j) in _lit:
				string += "#"
			elif (i, j) in _dark:
				string += "."
			else:
				string += default
	return string


if __name__ == '__main__':
	start = time.time()
	file = read("day20")
	cypher, image = file.split("\n\n")

	image = image.split("\n")

	lit = set()
	dark = set()
	for y in range(len(image)):
		for x in range(len(image[0])):
			if image[y][x] == "#":
				lit.add((x, y))
			else:
				dark.add((x, y))

	endless = "."
	iterations = 50
	for iteration in range(iterations):
		# print("iter: " + str(iteration + 1))
		new_lit = set()
		new_dark = set()

		if endless == ".":
			to_sort = lit
		else:
			to_sort = dark
		x_sort = sorted(to_sort, key=lambda pos: pos[0])
		min_x = x_sort[0][0] - 1
		max_x = x_sort[-1][0] + 1
		y_sort = sorted(to_sort, key=lambda pos: pos[1])
		min_y = y_sort[0][1] - 1
		max_y = y_sort[-1][1] + 1
		for x in range(min_x, max_x + 1):
			for y in range(min_y, max_y + 1):
				char = cypher[get_bin(build_string(x, y, lit, dark, endless))]
				if char == "#":
					new_lit.add((x, y))
				else:
					new_dark.add((x, y))
		lit = new_lit
		dark = new_dark

		if endless == ".":
			endless = cypher[0]
		else:
			endless = cypher[511]

	print(len(lit))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
