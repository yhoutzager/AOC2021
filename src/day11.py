from filereader import *
from gridhelper import *

def do_step(points):
	flashed = set()
	for point in points:
		points[point] += 1

	flashing = set(point for point, value in points.items() if value > 9)

	while flashing:
		point = flashing.pop()

		for neighbor in neighbours8(point):
			x, y = neighbor
			if x < 0 or y < 0 or x > 9 or y > 9:
				continue

			points[neighbor] += 1
			if points[neighbor] > 9 and neighbor not in flashed:
				flashing.add(neighbor)

		flashed.add(point)

	for point in flashed:
		points[point] = 0

	return flashed

if __name__ == '__main__':
	grid = as_grid(read_lines("day11"), True)
	print(grid.points)

	# points = dict()
	# for x, row in enumerate(read("day11").splitlines()):
	# 	for y, char in enumerate(row):
	# 		points[(x,y)] = int(char)
	# [[points.update((x,y): char) for x, char in enumerate(line)] for y,line in enumerate(read("test").splitlines())]

	# sum = 0
	# steps = 100
	# for _ in range(steps):
	# 	sum+=len(do_step(points))
	# print(sum)

	# steps = 0
	# while True:
	# 	steps += 1
	# 	flashed = do_step(points)
	# 	# if steps > 192:
	# 	# 	print("step " + str(steps))
	# 	# 	for x in range(10):
	# 	# 		print(''.join([str(points[(x,y)]) for y in range(10)]))
	# 	# 	print(flashed)
	# 	if len(points) == len(flashed):
	# 		break
	# 	# if steps > 200:
	# 	# 	break
	# print(steps)


