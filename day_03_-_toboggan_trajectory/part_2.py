#!/usr/bin/env python3

def solution(elements):
	total = 1
	for change_col, change_row in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
		col = 0
		trees = 0

		for r in range(0,len(elements),change_row):            
			trees += elements[r][col % len(elements[0])] == '#'
			col += change_col

		total *= trees

	return total

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print(f'Answer : {solution(inputs)}')