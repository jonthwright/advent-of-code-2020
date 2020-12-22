#!/usr/bin/env python3

def get_side(tile, side):
    if side == 'top':
        return tile[0]
    if side == 'bottom':
        return tile[-1][::-1]
    if side == 'right':
        return ''.join([t[-1] for t in tile])
    if side == 'left':
        return ''.join([t[0] for t in tile])[::-1]
    raise ValueError

def rotate(tile):
    R = len(tile)
    C = len(tile[0])
    new = [['x' for _ in range(C)] for _ in range(R)]
    for row in range(R):
        for col in range(C):
            new[row][col] = tile[C - col - 1][row]
    return [''.join(row) for row in new]

def add_fullpic(fullpic, tile, newline=False):
    if not fullpic:
        return tile.copy()
    elif newline:
        for row in tile:
            fullpic.append(row)
        return fullpic
    else:
        R = len(fullpic) - len(tile)
        for row in range(len(tile)):
            fullpic[row + R] += tile[row]
        return fullpic

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
	idx = None
 
	for raw_tile in elements:
		lines = raw_tile.strip('\n').split('\n')
		idx = int(lines[0].split()[1].strip(':'))
		sides = extract_sides((grid := lines[1:]))
		tiles[idx] = {'grid': grid, 'sides': sides, 'neighbours': {}}

		for i, tile in tiles.items():
			if i == idx:
				continue

			shared = [s for s in tile['sides'] if s in sides]

			for s in shared:
				tiles[idx]['neighbours'][i] = s
				tiles[i]['neighbours'][idx] = s

	corners = [int(tile) for tile in tiles if len(tiles[tile]['neighbours']) == 2]

	row, col = 0, 0
	grid_map = {}
	fullpic = []

	while not len(grid_map) == len(tiles):
		if row == 0 and col == 0:
			idx = corners[0]
			tile = tiles[idx]['grid']
			neighbours = list(tiles[idx]['neighbours'].values())
			neighbours += [n[::-1] for n in neighbours]

			while True:
				bottom, right = get_side(tile, 'bottom'), get_side(tile, 'right')

				if bottom in neighbours and right in neighbours:
					break

				tile = rotate(tile)

			grid_map[(row, col)] = idx
			tiles[idx]['grid'] = tile
			fullpic = add_fullpic(fullpic, tile)
			col += 1

		elif col == 0:
			p_idx = grid_map[(row - 1, col)]
			p_tile = tiles[p_idx]['grid']
			bot_tile = get_side(p_tile, 'bottom')

			side_options = [bot_tile, bot_tile[::-1]]

			idx = [i for i, s in tiles[p_idx]['neighbours'].items() if s in side_options][0]
			tile = tiles[idx]['grid']
			n_side = get_side(tiles[p_idx]['grid'], 'bottom')
			found = False

			for i in range(8):
				if i == 4:
					tile = tile[::-1]

				if get_side(tile, 'top') == n_side[::-1]:
					found = True
					break

				tile = rotate(tile)

			if not found:
				raise Exception

			grid_map[(row, col)] = idx
			tiles[idx]['grid'] = tile
			fullpic = add_fullpic(fullpic, tile, newline=True)
			col += 1

		else:
			p_idx = idx
			p_tile = tiles[p_idx]['grid']
			right_tile = get_side(p_tile, 'right')

			side_options = [right_tile, right_tile[::-1]]

			idx = [i for i, s in tiles[p_idx]['neighbours'].items() if s in side_options]

			if len(idx) == 1:
				idx = idx[0]
				tile = tiles[idx]['grid']
				n_side = get_side(tiles[p_idx]['grid'], 'right')
				found = False

				for i in range(8):
					if i == 4:
						tile = tile[::-1]

					if get_side(tile, 'left') == n_side[::-1]:
						found = True
						break

					tile = rotate(tile)

				if not found:
					raise Exception

				grid_map[(row, col)] = idx
				tiles[idx]['grid'] = tile
				fullpic = add_fullpic(fullpic, tile)
				col += 1

			elif len(idx) == 0:
				row, col = row + 1, 0

			else:
				raise Exception

	G = []
	for i in range(len(fullpic) // 10):
		G.extend(fullpic[(10 * i) + 1 : (10 * i) + 9])
	G = [''.join([row[(10 * col) + 1 : (10 * col) + 9] for col in range(len(row) // 10)]) for row in G]

	MONSTER = []
	MONSTER.append('                  # ')
	MONSTER.append('#    ##    ##    ###')
	MONSTER.append(' #  #  #  #  #  #   ')
	MONSTER = [(x,y) for x in range(20) for y in range(3) if MONSTER[y][x] == '#']

	mon = set()

	for i in range(8):
		if i == 4:
			G = G[::-1]

		for row in range(len(G) - 2):
			for col in range(len(G[0]) - 20):
				if all(G[row + row_off][col + col_off] == "#" for col_off, row_off in MONSTER):
					for col_off, row_off in MONSTER:
						mon.add((row + row_off, col + col_off))

		G = rotate(G)

	return len([col for row in G for col in row if col == "#"]) - len(mon)

if __name__ == '__main__':	
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split('\n\n')
	print('Day 20 : Jurassic Jigsaw - part 2')
	print(f'>>> Answer : {solution(inputs)}')