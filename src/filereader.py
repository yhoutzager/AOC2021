import typing


def open_file(name):
	return open("../input/" + name + ".txt", "r")


def read(name):
	return open_file(name).read()


def read_lines(name):
	return open_file(name).read().splitlines()


def read_split(name, delim):
	return open_file(name).read().split(sep=delim)


def read_comma_sep(name):
	return read_split(name, ",")


def trim(array):
	return [x.strip() for x in array]


def as_int(array):
	return [int(x) for x in array]


def as_grid(array, use_ints=False):
	points = dict()
	height = len(array)
	width = len(array[0])
	for x, row in enumerate(array):
		for y, char in enumerate(row):
			if use_ints:
				points[(x, y)] = int(char)
			else:
				points[(x, y)] = char

	return Grid(points, height, width)


def as_2d_array():
	return 0


def tuple_add(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return x1 + x2, y1 + y2


_neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
_neighbours8 = _neighbours + [(1, 1), (1, -1), (-1, -1), (-1, 1)]


class Grid:
	def __init__(
			self,
			points: typing.Dict[typing.Tuple[int, int], typing.Any],
			height: int,
			width: int,
	):
		self.points = points
		self.height = height
		self.width = width

	def __getitem__(self, point: typing.Tuple[int, int]):
		return self.points

	def __setitem__(self, point: typing.Tuple[int, int], value):
		self.points[point] = value

	def __len__(self):
		return len(self.points)

	def items(self):
		for point, value in self.points.items():
			yield point, value

	def neighbours(self, point: typing.Tuple[int, int]):
		for x in self.get_points_from_offset_list(_neighbours, point):
			yield x

	def neighbours8(self, point: typing.Tuple[int, int]):
		for x in self.get_points_from_offset_list(_neighbours8, point):
			yield x

	def get_points_from_offset_list(self, offset_list: typing.List[typing.Tuple[int, int]],
									point: typing.Tuple[int, int]):
		for add in offset_list:
			new_point = tuple_add(point, add)
			if new_point in self.points:
				yield new_point
