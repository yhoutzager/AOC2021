import statistics
from filereader import *

if __name__ == '__main__':
	# file = read_lines("test")
	file = read_lines("day10")

	open = ["(", "[", "{", "<"]
	close_map = {"(": ")", "[": "]", "{": "}", "<": ">"}

	table = {")": 3, "]": 57, "}": 1197, ">": 25137}
	table2 = {")": 1, "]": 2, "}": 3, ">": 4}

	illegals = []
	corrects = []
	scores = []
	for line in file:
		stack = []
		correct = True
		for char in line:
			if char in open:
				stack.append(char)
				continue
			last_open = stack.pop()
			if char != close_map[last_open]:
				illegals.append(table[char])
				correct = False
				break
		if correct:
			score = 0
			while len(stack) > 0:
				score = score * 5 + table2[close_map[stack.pop()]]
			scores.append(score)
	print(sum(illegals))
	print(statistics.median(scores))