from filereader import *


def rotate_vector(vector):
	roll = lambda x, y, z: (x, z, -y)
	turn = lambda x, y, z: (-y, x, z)

	vectors = []
	for c in range(2):
		for s in range(3):
			vector = roll(*vector)
			vectors.append(vector)
			for i in range(3):
				vector = turn(*vector)
				vectors.append(vector)
		vector = roll(*turn(*roll(*vector)))
	return vectors


def rotate_vectors_yield(vectors):
	roll = lambda x, y, z: (x, z, -y)
	turn = lambda x, y, z: (-y, x, z)

	for c in range(2):
		for s in range(3):
			vectors = [roll(*vector) for vector in vectors]
			yield vectors
			for i in range(3):
				vectors = [turn(*vector) for vector in vectors]
				yield vectors
		vectors = [roll(*turn(*roll(*vector))) for vector in vectors]

def man_dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def diff(a, b):
	return a[0] - b[0], a[1] - b[1], a[2] - b[2]

def add(a, b):
	return a[0] + b[0], a[1] + b[1], a[2] + b[2]
	

def offset_points(offset, beacons):
	new_beacons = []
	for beacon in beacons:
		new_beacons.append((beacon[0] + offset[0], beacon[1] + offset[1], beacon[2] + offset[2]))
	return new_beacons

def compare_scanner(a, b):
	for b_rot in rotate_vectors_yield(b):
		counter = 0
		for ai1 in range(len(a)):
			if (len(a) - ai1 + counter) < 12:
				break
			a1_count = 0
			for ai2 in range(ai1 + 1, len(a)):
				if (len(a) - ai1 + a1_count) < 12:
					break
				found = False
				for bi1 in range(len(b_rot)):
					for bi2 in range(bi1 + 1, len(b_rot)):
						if diff(a[ai1], a[ai2]) == diff(b_rot[bi1], b_rot[bi2]):
							counter += 1
							a1_count += 1
							if counter == 12:
								offset = (a[ai1][0] - b_rot[bi1][0], a[ai1][1] - b_rot[bi1][1], a[ai1][2] - b_rot[bi1][2])
								return offset_points(offset, b_rot), offset
							found = True
							break
					if found:
						break


	return None, None


if __name__ == '__main__':
	scanners = read("day19").split("\n\n")

	scanners = [[tuple(int(x) for x in coor.split(",")) for coor in scanner.split("\n")[1:]] for scanner in scanners]

	scanners_done = [False] * len(scanners)
	scanners_done[0] = True
	found_scanners = [[]] * len(scanners)
	found_scanners[0] = scanners[0]
	offsets = [()] * len(scanners)
	offsets[0] = (0,0,0)
	already_checked = set()

	while not all(scanners_done):
		for i in range(len(scanners)):
			if not scanners_done[i]:
				continue
			for j in range(len(scanners)):
				if i == j:
					continue
				if (i, j) in already_checked or (j, i) in already_checked:
					continue
				if scanners_done[j]:
					continue
				new_scanner, offset = compare_scanner(found_scanners[i], scanners[j])
				print(i, j, new_scanner, offset)
				already_checked.add((i, j))
				if new_scanner is not None:
					scanners_done[j] = True
					found_scanners[j] = new_scanner
					offsets[j] = offset
					print(offsets)
					print(offset)

					
	beacons = set()
	[[beacons.add(beacon) for beacon in scanner] for scanner in found_scanners]
	print(len(beacons))

	max_dist = 0
	for i in range(len(offsets)):
		for j in range(i+1, len(offsets)):
			dist = man_dist(offsets[i], offsets[j])
			print(dist)
			if dist > max_dist:
				max_dist = dist
	print(max_dist)


