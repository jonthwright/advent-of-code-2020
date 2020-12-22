#!/usr/bin/env python3

def solution(elements):
	elements.sort()
	
	for i in range(len(elements) - 2):
		if i > 0 and elements[i] == elements[i-1]:
			continue
		l, r = i + 1, len(elements) - 1
		
		while (l < r):
			total = elements[i] + elements[l] + elements[r]
			l += total < 2020
			r -= total > 2020

			if total == 2020:
				return elements[i] * elements[l] * elements[r]
	return -1

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readlines()]
	print('Day 01 : Report Repair - part 2')
	print(f'>>> Answer : {solution(inputs)}')