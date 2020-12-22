#!/usr/bin/env python3

def solution(elements):
	elements = set(elements)
	for elem in elements:
		comp = 2020 - elem
		if comp in elements:
			return elem * comp
	return -1

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readlines()]
	print('Day 01 : Report Repair - part 1')
	print(f'>>> Answer : {solution(inputs)}')