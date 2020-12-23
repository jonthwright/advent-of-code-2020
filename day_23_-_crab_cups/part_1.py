#!/usr/bin/env python3

import math

def step(cups):
	cups_num = len(cups)
	pick = [cups.pop(1) for _ in range(3)]

	cup_temp = sorted(cups)
	dest = cup_temp[(cup_temp.index(cups[0]) - 1) % (cups_num - 3)]
	dest_idx = cups.index(dest) + 1

	return cups[1:dest_idx] + pick + cups[dest_idx:] + cups[0:1]

def solution(numbers):
	for _ in range(100):
		numbers = step(numbers)

	one = numbers.index(1)
	numbers = numbers[one + 1:] + numbers[:one]

	return (''.join(str(num) for num in numbers))


if __name__ == '__main__':
	number = 398254716
	number = [int(num) for num in str(number)]

	print('Day 23 : Crab Cups - part 1')
	print(f'>>> Answer : {solution(number)}')