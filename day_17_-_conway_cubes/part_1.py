#!/usr/bin/env python3

def stringify(*args):
	s = ''

	for x in args:
		s += f'{x},'

	return s[:-1]

def unstringify(str_node):
    return [int(coords) for coords in str_node.split(',')]

def get_neighbours(node):
	x, y, z = unstringify(node)

	for x_delta in range(-1, 2):
		for y_delta in range(-1, 2):
			for z_delta in range(-1, 2):
				if x_delta != 0 or y_delta != 0 or z_delta != 0:
					yield stringify(x + x_delta, y + y_delta, z + z_delta)

def step(active_nodes):
	new_nodes = set()
	activation_counts = {}

	for node in active_nodes:
		neighbours_count = 0
		for neighbour_str in get_neighbours(node):
			if neighbour_str in active_nodes:
				neighbours_count += 1
			else:
				if neighbour_str not in activation_counts:
					activation_counts[neighbour_str] =  0
				activation_counts[neighbour_str] += 1
		
		if 1 < neighbours_count <= 3:
			new_nodes.add(node)

	for neigh, count in activation_counts.items():
		if count == 3:
			new_nodes.add(neigh)

	return new_nodes

def solution(elements):
	nodes = set()
	for x in range(len(elements)):
		for y in range(len(elements[0])):
			if elements[x][y] == '#':
				nodes.add(stringify(x, y, 0, 0))

	for _ in range(6):
		nodes = step(nodes)

	return len(nodes)
	
if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [x.strip('\n') for x in f.readlines()]
	print(f'Answer : {solution(inputs)}')