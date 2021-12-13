from collections import defaultdict

from filereader import *


def go_to_next(current, visited, did_double):
	if current == "end":
		return 1
	_paths = 0
	visited[current] += 1
	for x in graph[current]:
		if x.isupper() or visited[x] == 0:
			_paths += go_to_next(x, visited, did_double)
		elif x != "start" and visited[x] == 1 and not did_double:
			_paths += go_to_next(x, visited, True)
	visited[current] -= 1

	return _paths


if __name__ == '__main__':
	file = read_lines("day12")
	# file = read_lines("test")

	graph = {}
	points = set()
	visited = {}
	for x in file:
		a, b = x.split("-")
		if a in graph:
			graph[a].append(b)
		else:
			graph[a] = [b]
		if b in graph:
			graph[b].append(a)
		else:
			graph[b] = [a]
		visited[a], visited[b] = 0, 0

	paths = go_to_next("start", visited, False)

	print(paths)



