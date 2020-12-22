#!/usr/bin/env python3

import re

def solution(elements):
	valid = 0

	for elem in elements:
		regex = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', elem)
		min_, max_, ltr, password = int(regex.group(1)), int(regex.group(2)), regex.group(3), regex.group(4)

		count = 0
		for c in password:
			count += c == ltr

		valid += min_ <= count <= max_
	
	return valid

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
	print('Day 02 : Password Philosophy - part 1')
	print(f'>>> Answer : {solution(inputs)}')