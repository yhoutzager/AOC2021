from filereader import *

if __name__ == '__main__':
	file = read_lines("day15")

	grid = as_grid(file, True)
	unvisited = {node: None for node in grid.points}
	visited = {}

	start = (0, 0)
	currentDistance = 0
	unvisited[start] = currentDistance

	currentPoint = start
	while True:
		for neighbour in grid.neighbours(currentPoint):
			if neighbour not in unvisited:
				continue
			newDistance = currentDistance + grid.points[neighbour]
			if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
				unvisited[neighbour] = newDistance
		visited[currentPoint] = currentDistance
		del unvisited[currentPoint]
		if not unvisited:
			break
		candidates = [point for point in unvisited.items() if point[1]]
		currentPoint, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

	size = grid.width -1
	print(visited[size, size])



