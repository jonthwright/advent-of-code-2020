#!/usr/bin/env python3

from collections import defaultdict
import re

def solution(elements):
	tiles = defaultdict(bool)

	for elem in elements:
		coords = re.findall(r'e|se|sw|w|nw|ne', elem)
		ns = coords.count('se') + coords.count('sw') - coords.count('ne') - coords.count('nw')
		we = coords.count('e') + coords.count('ne') - coords.count('w') - coords.count('sw')
		tiles[(ns, we)] = not tiles[(ns, we)]

	return sum(v for v in tiles.values())

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [line for line in f.read().splitlines()]
	print('Day 24 : Lobby Layout - part 1')
	print(f'>>> Answer : {solution(inputs)}')