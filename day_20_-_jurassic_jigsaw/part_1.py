#!/usr/bin/env python3

def reduce(func, lst, acc):
    for e in lst:
        acc = func(e, acc)
    return acc

def extract_sides(grid):
	sides = set()
	sides.add(grid[0])
	sides.add(grid[-1]) 
	sides.add(''.join(g[0] for g in grid))
	sides.add(''.join(g[-1] for g in grid))

	for side in sides.copy():
		sides.add(side[::-1])

	return sides

def solution(elements):
	tiles = {}

	for raw_tile in elements:
		lines = raw_tile.strip('\n').split('\n')
		idx = int(lines[0].split()[1].strip(':'))
		sides = extract_sides(lines[1:])
		tiles[idx] = {'sides': sides, 'neighbours': {}}

		for i, tile in tiles.items():
			if i == idx:
				continue

			shared = [s for s in tile['sides'] if s in sides]

			for s in shared:
				tiles[idx]['neighbours'][i] = s
				tiles[i]['neighbours'][idx] = s

	corners = [int(tile) for tile in tiles if len(tiles[tile]['neighbours']) == 2]
 
	return reduce(lambda x, y: x * y, corners, 1)

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split("\n\n")
	print('Day 20 : Jurassic Jigsaw - part 1')
	print(f'>>> Answer : {solution(inputs)}')