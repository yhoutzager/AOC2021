from filereader import *

if __name__ == '__main__':
	# file = read_lines("test")
	file = read_lines("day02")
	commands = [x.split(" ") for x in file]

	pos_x, pos_y1, pos_y2, aim = 0, 0, 0, 0
	for command in commands:
		action = command[0]
		mag = int(command[1])
		if action == "forward":
			pos_x += mag
			pos_y2 += aim * mag
		elif action == "down":
			aim += mag
			pos_y1 += mag
		elif action == "up":
			aim -= mag
			pos_y1 -= mag

	print(pos_x * pos_y1)
	print(pos_x * pos_y2)