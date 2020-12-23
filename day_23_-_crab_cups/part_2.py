#!/usr/bin/env python3

import math

def gen_cups(cups):
	lngth = 1000000
	cuplist = {}
	
	for i in range(lngth):
		if i < len(cups) - 1:
			cuplist[cups[i]] = cups[i + 1]
		elif i == len(cups) - 1 and len(cups) == lngth:
			cuplist[cups[i]] = cups[0]
		elif i == len(cups) - 1 and len(cups) < lngth:
			cuplist[cups[i]] = max(cups) + 1
		elif i < lngth - 1:
			cuplist[i + 1] = i + 2
		elif i == lngth - 1:
			cuplist[i + 1] = cups[0]
	
	return cuplist

def step(cups, ptr):
	first_cup = cups[ptr]
	second_cup = cups[first_cup]
	third_cup = cups[second_cup]
	
	dest = ((ptr - 2) % 1000000) + 1
	while dest in (first_cup, second_cup, third_cup):
		dest = ((dest - 2) % 1000000) + 1
	
	cups[ptr], cups[third_cup], cups[dest] = cups[third_cup], cups[dest], first_cup

	return cups[ptr]
	
def solution(numbers):
	cups = gen_cups(numbers)
	cup = numbers[0]

	for _ in range(10000000):
		cup = step(cups, cup)

	return cups[1] * cups[cups[1]]

if __name__ == '__main__':
	number = 398254716
	number = [int(num) for num in str(number)]
	
	print('Day 23 : Crab Cups - part 2')
	print(f'>>> Answer : {solution(number)}')