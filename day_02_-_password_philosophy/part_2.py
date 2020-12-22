#!/usr/bin/env python3

import re

def solution(elements):
	valid = 0

	for elem in elements:
		regex = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', elem)
		i, j, ltr, password = int(regex.group(1)), int(regex.group(2)), regex.group(3), regex.group(4)
		valid += (password[i - 1] == ltr) ^ (password[j - 1] == ltr)
	
	return valid


if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
	print('Day 02 : Password Philosophy - part 2')
	print(f'>>> Answer : {solution(inputs)}')