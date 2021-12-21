from filereader import *

sumofversions=0

def type_four(string, pos):
	list = []
	while True:
		if type == 4:
			leading = mapped[pos]
			literal = mapped[pos + 1: pos + 5]
			list.append(literal)
			if leading == "0":
				break
			pos += 5
	return ''.join([x for x in list])

def parse(data):
	global sumofversions
	version = int(data[:3], 2)
	data = data[3:]
	sumofversions += version
	type = int(data[:3], 2)
	data = data[3:]

	if type == 4:
		value = ""
		while True:
			check = data[0]
			value += data[1:5]
			data = data[5:]
			if check == "0":
				break
	else:
		length_type_id = data[0]
		data = data[1:]
		if length_type_id == "0":
			length = data[:15]
			data = data[15:]
			sub_length = int(length, 2)
			sub_packets = data[:sub_length]
			while sub_packets:
				sub_packets = parse(sub_packets)
			data = data[sub_length:]
		else:
			length = data[:11]
			data = data[11:]
			sub_packet_times = int(length, 2)
			for i in range(sub_packet_times):
				data = parse(data)
	return data

if __name__ == '__main__':
	file = read("test")
	map = {
		"0": "0000",
		"1": "0001",
		"2": "0010",
		"3": "0011",
		"4": "0100",
		"5": "0101",
		"6": "0110",
		"7": "0111",
		"8": "1000",
		"9": "1001",
		"A": "1010",
		"B": "1011",
		"C": "1100",
		"D": "1101",
		"E": "1110",
		"F": "1111",
	}
	mapped = "".join([map[x] for x in file])
	print(mapped)
	parse(mapped)
	print(sumofversions)
