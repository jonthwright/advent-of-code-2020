#!/usr/bin/env python3

import re

def has_shiny_gold(colour, bags):
	if colour == "shiny gold": 
		return True
	return any(has_shiny_gold(c, bags) for _, c in bags[colour])

def solution(inputs):
	bags = {}
	bag_count = 0

	for line in inputs:
		colour = re.match(r"(.+?) bags contain", line)[1]  
		bags[colour] = re.findall(r"(\d+?) (.+?) bags?", line)

	for bag in bags:
		bag_count += has_shiny_gold(bag, bags)

	return bag_count - 1

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 07 : Handy Haversacks - part 1')
	print(f'>>> Answer : {solution(inputs)}')