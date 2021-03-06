#!/usr/bin/env python3

import math

def solution(elements):
	direction = 90
	x, y = 0, 0
	wx, wy = 10, 1
	
	for cmd in elements:
		instruction, units = cmd[0], int(cmd[1:	])
		if instruction == 'N':
			wy += units
		elif instruction == 'S':
			wy -= units
		elif instruction == 'E':
			wx += units
		elif instruction == 'W':
			wx -= units
		elif instruction == 'L':
			wx_ = wx
			wx = round((math.cos(math.radians(units)) * wx) - (math.sin(math.radians(units)) * wy))
			wy = round((math.sin(math.radians(units)) * wx_) + (math.cos(math.radians(units)) * wy))
		elif instruction == 'R':
			wx_ = wx
			wx = round((math.cos(math.radians(360 - units)) * wx) - (math.sin(math.radians(360 - units)) * wy))
			wy = round((math.sin(math.radians(360 - units)) * wx_) + (math.cos(math.radians(360 - units)) * wy))
		elif instruction == 'F':
			x += wx * units
			y += wy * units

	return abs(x) + abs(y)

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 12 : Rain Risk - part 2')
	print(f'>>> Answer : {solution(inputs)}')