from filereader import *

def fold(fold):
	global points
	new_points = set()
	if (fold[0] == 'x'):
		for x, y in points:
			if x > fold[1]:
				new_x = 2 * fold[1] - x
				new_points.add((new_x, y))
			else:
				new_points.add((x, y))
	elif (fold[0] == 'y'):
		for x, y in points:
			if y > fold[1]:
				new_y = 2 * fold[1] - y
				new_points.add((x, new_y))
			else:
				new_points.add((x, y))
	points = new_points

if __name__ == '__main__':
	file = read("day13")
	points_f, folds_f = file.split("\n\n")

	folds_f = [line for line in folds_f.split("\n")]
	folds = []
	for line in folds_f:
		i = line.find("=")
		folds.append((line[i-1], int(line[i+1:])))

	points = set()
	for point in points_f.split("\n"):
		x, y = point.split(",")
		points.add((int(x), int(y)))

	for x in folds:
		fold(x)
	w = max([x for x, y in points]) + 1
	h = max([y for x, y in points]) + 1

	string = ""
	for y in range(h):
		for x in range(w):
			if (x, y) in points:
				string += "█"
			else:
				string += " "
		string += "\n"

	print(string)

