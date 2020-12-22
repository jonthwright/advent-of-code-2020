#!/usr/bin/env python3

import re

def solution(elements):
	valid = 0

	for (min_, max_, ltr, password) in elements:
		count = 0
		for c in password:
			if c == ltr:
				count += 1
		valid += min_ <= count <= max_
	
	return valid

def process_inputs(inputs):
	output = []
	for i in inputs:
		regex = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', i)
		output.append((int(regex.group(1)), int(regex.group(2)), regex.group(3), regex.group(4)))
	return output

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
	processed = process_inputs(inputs)
	print(f'Answer : {solution(processed)}')