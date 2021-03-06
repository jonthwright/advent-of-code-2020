#!/usr/bin/env python3

def solution(elements):
	convert = lambda x : x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
	elements = set(convert(e) for e in elements)
	return max(int(s, 2) for s in elements)

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 05 : Binary Boarding - part 1')
	print(f'>>> Answer : {solution(inputs)}')