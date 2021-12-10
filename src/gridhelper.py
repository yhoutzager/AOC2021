_neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
_neighbours8 = _neighbours + [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def neighbours(point):
	for add in _neighbours:
		yield tuple_add(point, add)

def neighbours8(point):
	for add in _neighbours8:
		yield tuple_add(point, add)

def tuple_add(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return (x1 + x2, y1 + y2)
