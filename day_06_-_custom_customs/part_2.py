#!/usr/bin/env python3

import string

def solution(elements):
	count = 0
	
	for elem in elements:
		ind_elem = elem.split("\n")
		for c in string.ascii_lowercase:
			count += all([c in a for a in ind_elem])
	
	return count

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split('\n\n')
	print('Day 06 : Custom Customs - part 2')
	print(f'>>> Answer : {solution(inputs)}')