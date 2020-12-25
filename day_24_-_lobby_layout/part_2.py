#!/usr/bin/env python3

from collections import defaultdict
import re

def tiling_changes(tilings):
	new_tiles = defaultdict(bool)
	adjacent = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]

	for k, v in tilings.items():
		for adj in adjacent:
			tile = (k[0] + adj[0], k[1] + adj[1])
			new_tiles[tile] = tilings.get(tile, False)

	for k, v in new_tiles.items():
		neigh = sum(tilings[(k[0] + adj[0], k[1] + adj[1])] for adj in adjacent)
		if v and not neigh or neigh > 2:
			new_tiles[k] = False
		else:
			new_tiles[k] = True if neigh == 2 else new_tiles[k]

	return new_tiles

def solution(elements):
	tiles = defaultdict(bool)

	for elem in elements:
		coords = re.findall(r'e|se|sw|w|nw|ne', elem)
		ns = coords.count('se') + coords.count('sw') - coords.count('ne') - coords.count('nw')
		we = coords.count('e') + coords.count('ne') - coords.count('w') - coords.count('sw')
		tiles[(ns, we)] = not tiles[(ns, we)]

	for _ in range(100):
		tiles = tiling_changes(tiles)

	return sum(v for v in tiles.values())

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [line for line in f.read().splitlines()]
	print('Day 24 : Lobby Layout - part 2')
	print(f'>>> Answer : {solution(inputs)}')