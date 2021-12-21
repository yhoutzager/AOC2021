import time

if __name__ == '__main__':
	# x_min, x_max, y_min, y_max = 29, 73, -248, -194
	x_min, x_max, y_min, y_max = 257, 286, -101, -57
	# x_min, x_max, y_min, y_max = 20, 30, -10, -5

	start = time.time()
	dx = lambda x: x + 1 if x < 0 else x - 1 if x > 0 else x
	dy = lambda y: y - 1

	test = abs(y_min)

	x_starts = []
	for vxs in range(x_max + 1):
		x = 0
		v = vxs
		steps = 0
		while v > 0 and x < x_max:
			x += v
			steps += 1
			v = dx(v)
			if x_min <= x <= x_max:
				x_starts.append(vxs)

	y_starts = []
	for vys in range(y_min, test):
		y = 0
		vy = vys
		if vy > 0:
			vy = -vy - 1
		while y > y_min:
			y += vy
			vy = dy(vy)
			if y_max >= y >= y_min:
				y_starts.append(vys)

	hits_v = set()
	for vxs in x_starts:
		for vys in y_starts:
			vx, vy = vxs, vys
			x, y = 0, 0
			while y > y_min and x < x_max:
				x += vx
				y += vy
				vx = dx(vx)
				vy = dy(vy)
				if x_min <= x <= x_max and y_max >= y >= y_min:
					hits_v.add((vxs, vys))
					break

	print(len(hits_v))
	# print(hits_v)
	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))