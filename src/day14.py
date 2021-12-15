from collections import Counter

from filereader import *

if __name__ == '__main__':
	file = read_lines("day14")
	temp = file[0]
	pairs = dict()
	pairs2 = dict()
	for x in file[2:]:
		k,v = x.split(" -> ")
		pairs[k] = k[0] + v + k[1]
		pairs2[k] = (k[0] + v, v + k[1])

	# for step in range(10):
	# 	new_temp = ""
	# 	for i in range(len(temp) - 1):
	# 		piece = temp[i:i+2]
	# 		if piece in pairs:
	# 			new_temp += pairs[piece][:2]
	# 		else:
	# 			new_temp += piece[:1]
	#
	# 	new_temp += temp[-1]
	# 	temp = new_temp
	# 	print(step, len(temp))
	# count = Counter(temp)
	# _min = count[min(count, key = count.get)]
	# _max = count[max(count, key = count.get)]
	# ans = _max - _min
	# print(ans)

	counter = Counter()
	for i in range(len(temp)-1):
		counter[temp[i] + temp[i + 1]] += 1
	print(counter)

	for steps in range(40):
		new_counter = Counter()
		for pair in counter:
			new_counter[pairs2[pair][0]] += counter[pair]
			new_counter[pairs2[pair][1]] += counter[pair]
		counter = new_counter

	counter_letters = Counter()
	for pair in counter:
		counter_letters[pair[0]] += counter[pair]
	counter_letters[temp[-1]] += 1
	print(max(counter_letters.values())-min(counter_letters.values()))


