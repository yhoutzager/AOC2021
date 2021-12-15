import time

from heapq import heappop, heappush
from typing import Dict, List, Tuple

Pair = Tuple[int, int]
Graph = Dict[Pair, int]


from filereader import *

def dijkstra(grid: Grid, start: Pair, end: Pair) -> Dict[Pair, int]:
	dist: Dict[Pair, int] = {start: 0}
	priority_queue: List[Tuple[int, Pair]] = []

	for v in grid.keys():
		if v != start:
			dist[v] = int(1e9)
		heappush(priority_queue, (dist[v], v))

	while priority_queue:
		_, point = heappop(priority_queue)
		if point == end:
			return dist
		for neighbour in grid.neighbours(point):
			if neighbour not in grid:
				continue
			alt = dist[point] + grid[point]
			if alt < dist[neighbour]:
				dist[neighbour] = alt
				heappush(priority_queue, (alt, neighbour))

if __name__ == '__main__':
	start_time = time.time()
	file = read_lines("day15")

	grid = as_grid(file, True)

	size = grid.width
	new_points = {}
	for i in range(5):
		for j in range(5):
			for point, value in grid.points.items():
				new_value = value + i + j
				while new_value > 9:
					new_value -= 9
				new_points[(point[0]+size*i, point[1]+size*j)] = new_value

	grid = Grid(new_points, size * 5, size * 5)
	end_time = time.time()

	unvisited = {node: None for node in grid.points}
	visited = {}

	start = (0, 0)
	end = (grid.width - 1, grid.height - 1)
	dist = dijkstra(grid, start, end)
	print(dist[end])

	end_time = time.time()
	print('Time: {:.3f} s'.format(end_time - start_time))



