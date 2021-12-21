from filereader import *

DIGITS = '0123456789'


def add(a, b):
	return [a, b]


def try_explode(num):
	num_str = str(num).replace(' ', '')
	depth = 0
	for idx, c in enumerate(num_str):
		if c == '[':
			depth += 1
			if depth == 5:
				# Explode!
				end_idx = num_str.find(']', idx)
				l, r = [int(x) for x in num_str[idx + 1:end_idx].split(',')]
				left = num_str[:idx]
				for lidx in range(len(left) - 1, -1, -1):
					c = left[lidx]
					if c in DIGITS:
						term = max(i for i in range(lidx)
								   if left[i] not in DIGITS)
						val = int(left[term + 1:lidx + 1])
						val += l
						left = left[:term + 1] + str(val) + left[lidx + 1:]
						break
				mid = '0'
				right = num_str[end_idx + 1:]
				for ridx, c in enumerate(right):
					if c in DIGITS:
						term = min(i for i in range(ridx + 1, len(right))
								   if right[i] not in DIGITS)
						val = int(right[ridx:term])
						val += r
						right = right[:ridx] + str(val) + right[term:]
						break
				return eval(left + mid + right)
		elif c == ']':
			depth -= 1
	return None


def try_split(num):
	if isinstance(num, list):
		a, b = num
		new_a = try_split(a)
		if new_a is not None:
			return [new_a, b]
		new_b = try_split(b)
		if new_b is not None:
			return [a, new_b]
		return None
	if num > 9:
		d, m = divmod(num, 2)
		return [d, d + m]
	return None


def reduce(_sum):
	while True:
		new_sum = try_explode(_sum)
		if new_sum is not None:
			_sum = new_sum
			continue
		new_sum = try_split(_sum)
		if new_sum is not None:
			_sum = new_sum
			continue
		return _sum


def magnitude(num):
	if isinstance(num, list):
		a, b = num
		a = magnitude(a)
		b = magnitude(b)
		return 3 * a + 2 * b
	return num


if __name__ == '__main__':
	file = read_lines("day18")

	sum_list = list(map(eval, file))
	num = sum_list[0]

	for item in sum_list[1:]:
		item = reduce(item)
		num = reduce(add(num, item))

	answer = magnitude(num)

	print(answer)

	sum_list = list(map(reduce, sum_list))

	best = 0
	for ia, a in enumerate(sum_list):
		for ib, b in enumerate(sum_list):
			if ia == ib:
				continue

			mag = magnitude(reduce(add(a, b)))
			best = max(best, mag)

	answer = best

	print(answer)
