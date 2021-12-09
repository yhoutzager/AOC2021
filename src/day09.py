from filereader import *

def is_low_point(grid, x , y):
	if 0 < x and grid[x-1][y] <= grid[x][y]:
		return False
	if x < len(grid) - 1 and grid[x+1][y] <= grid[x][y]:
		return False
	if 0 < y and grid[x][y-1] <= grid[x][y]:
		return False
	if y < len(grid[0]) - 1 and grid[x][y+1] <= grid[x][y]:
		return False
	return True

def basin_crawler(grid, x, y, visited):
	sum = 0
	if (x,y) in visited or x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
		return sum
	if grid[x][y] == 9:
		return sum

	sum += 1
	visited.append((x, y))
	for dx in (-1, 1):
		sum += basin_crawler(grid, x + dx, y , visited)
	for dy in (-1, 1):
		sum += basin_crawler(grid, x, y + dy, visited)
	return sum

if __name__ == '__main__':
	# file = read_lines("test")
	file = read_lines("day09")
	grid = [[int(y) for y in x] for x in file]

	sum = 0
	low_points = []
	for y in range(len(grid[0])):
		for x in range(len(grid)):
			if is_low_point(grid, x, y):
				sum += grid[x][y] + 1
				low_points.append((x,y))

	basin_sizes = []
	for x, y in low_points:
		visited = []
		basin_size = basin_crawler(grid, x, y, visited)
		print(x, y, basin_size)

		basin_sizes.append(basin_size)

	ans = 1
	for x in sorted(basin_sizes)[-3:]:
		ans *= x

	print(ans)


	print(sum)