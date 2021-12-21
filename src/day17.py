if __name__ == '__main__':
	# x_min, x_max, y_min, y_max = 29, 73, -248, -194
	x_min, x_max, y_min, y_max = 20, 30, -10, -5

	start = (0, 0)
	dx = lambda x : x + 1 if x < 0 else x - 1 if x > 0 else x
	dy = lambda y : y - 1

	# stops_in_zone = []
	# i = 0
	# while True:
	# 	i += 1
	# 	steps = 0
	# 	v = i
	# 	pos = 0
	# 	outerbreak = False
	# 	while v > 0:
	# 		pos += v
	# 		v = dx(v)
	# 		if v == 0 and x_min < pos < x_max:
	# 			stops_in_zone.append(i)
	# 			break
	# 		if v == 0:
	# 			break
	# 		if pos > x_max:
	# 			outerbreak = True
	# 			break
	# 	if outerbreak:
	# 		break

	top_height = 0
	for i in range(1000):
		v = i
		pos = 0
		height = 0
		hit = False
		while pos > y_min:
			pos += v
			if y_max >= pos >= y_min:
				hit = True
				break
			if pos > height:
				height = pos
			v = dy(v)
		if hit and height > top_height:
			print(i)
			top_height = height

	print(top_height)