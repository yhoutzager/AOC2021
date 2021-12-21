from filereader import *


class sumpart:
	def __init__(
			self,
			depth,
			parts
	):
		self.depth = depth
		self.parts = parts


def find_subpart_index(part):
	count = 1
	i = 1
	while count > 0:
		if part[i] == "[":
			count += 1
		elif part[i] == "]":
			count -= 1
		i += 1
	return i


def parse_row(part, depth):
	parts = []
	while part:
		if part[0] == "[":
			i = find_subpart_index(part)
			subpart = part[1: i]
			parts.append(parse_row(subpart, depth + 1))
			part = part[i:]
		elif part[0] == "]":
			part = part[1:]
			break
		elif part[0] == ",":
			part = part[1:]
			continue
		else:
			closing_index = min([part.find(","), part.find("]")])
			parts.append(int(part[0: closing_index]))
			part = part[closing_index:]
	return sumpart(depth, parts)


if __name__ == '__main__':
	file = read_lines("test")

	test = parse_row(file[0], 0)
	print(test)
