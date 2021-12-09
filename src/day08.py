from filereader import *

if __name__ == '__main__':
	# file = read_lines("test")
	file = read_lines("day08")

	ans = 0
	numbers = []
	for line in file:
		left, right = line.split(" | ")
		left = [''.join(sorted(x)) for x in left.split(" ")]
		right = [''.join(sorted(x)) for x in right.split(" ")]

		map = dict()
		map[1] = next(x for x in left if len(x) == 2)
		map[7] = next(x for x in left if len(x) == 3)
		map[4] = next(x for x in left if len(x) == 4)
		map[8] = next(x for x in left if len(x) == 7)
		map[6] = next(x for x in left if len(x) == 6 and any(c not in x for c in map[1]))
		map[9] = next(x for x in left if len(x) == 6 and all(c in x for c in map[4]))
		map[0] = next(x for x in left if len(x) == 6 and x not in map.values())
		map[5] = next(x for x in left if len(x) == 5 and all(c in map[6] for c in x))
		map[3] = next(x for x in left if len(x) == 5 and all(c in map[9] for c in x) and x not in map.values())
		map[2] = next(x for x in left if len(x) == 5 and x not in map.values())

		numbers = {v:k for k, v in map.items()}
		ans += int("".join(str(numbers[r]) for r in right))



	print(ans)
	# print(sum(numbers))
