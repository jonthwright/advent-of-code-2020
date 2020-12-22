#!/usr/bin/env python3

def solution(chairs):
	row, col = len(chairs), len(chairs[0])
	neighbours = [(r,c) for c in range(-1, 2) for r in range(-1, 2) if not (r == 0 and c == 0)]
	next_chairs = [["x" for c in range(col)] for r in range(row)]

	while True:
		changed = False
		for r in range(row):
			for c in range(col):
				occupied_num = 0
				for dr, dc in neighbours:
					x = c + dc
					y = r + dr

					while 0 <= x < col and 0 <= y < row and chairs[y][x] == ".":
						x += dc
						y += dr

					if 0 <= x < col and 0 <= y < row and chairs[y][x] == "#":
						occupied_num += 1
				
				if chairs[r][c] == "L" and occupied_num == 0:
					next_chairs[r][c] = "#"
					changed = True
				elif chairs[r][c] == "#" and occupied_num >= 5:
					next_chairs[r][c] = "L"
					changed = True
				else:
					next_chairs[r][c] = chairs[r][c]

		if not changed:
			break

		chairs = [next_chair.copy() for next_chair in next_chairs]

	return sum(sum(chairs[r][c] == "#" for c in range(col)) for r in range(row))

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 11 : Seating System - part 2')
	print(f'>>> Answer : {solution(inputs)}')