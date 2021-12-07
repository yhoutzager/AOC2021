def open_file(name):
	return open("../input/" + name + ".txt", "r")

def read(name):
	return open_file(name).read()

def read_lines(name):
	return open_file(name).read().splitlines()

def read_split(name, delim):
	return open_file(name).read().split(sep=delim)

def read_comma_sep(name):
	return read_split(name, ",")

def trim(array):
	return [x.strip() for x in array]

def as_int(array):
	return [int(x) for x in array]