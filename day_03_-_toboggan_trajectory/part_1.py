#!/usr/bin/env python3

def solution(elements):
	slopeX, slopeY = 3, 1
	col = 0
	trees = 0

	for row in range(len(elements)):
		trees += elements[row][col % len(elements[0])] == '#'
		col += 3

	return trees

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
	print(f'Answer : {solution(inputs)}')