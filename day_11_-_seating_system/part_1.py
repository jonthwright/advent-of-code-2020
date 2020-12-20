def solution(chairs):
	row, col = len(chairs), len(chairs[0])
	neighbours = [(r,c) for c in range(-1, 2) for r in range(-1, 2) if not (r == 0 and c == 0)]
	next_chairs = [["x" for c in range(col)] for r in range(row)]

	while True:
		changed = False
		for r in range(row):
			for c in range(col):
				occupied_num = sum(chairs[row_][col_] == '#' for r_, c_ in neighbours if 0 <= (row_ := r + r_) < row and 0 <= (col_ := c + c_) < col)
				if chairs[r][c] == "L" and occupied_num == 0:
					next_chairs[r][c] = "#"
					changed = True
				elif chairs[r][c] == "#" and occupied_num >= 4:
					next_chairs[r][c] = "L"
					changed = True
				else:
					next_chairs[r][c] = chairs[r][c]

		if not changed:
			break

		chairs = [next_chair.copy() for next_chair in next_chairs]

	return sum(sum(chairs[r][c] == "#" for c in range(col)) for r in range(row))

def main():	
	with open('input_file.txt', 'r') as f:
		inputs = [e for e in f.read().strip().splitlines()]
	print(f'Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()