#!/usr/bin/env python3

def find(ans, bus_value, bus_offset, acc):
	while True:
		if (ans + bus_offset) % bus_value == 0:
			return ans
		ans += acc

def solution(elements):
	buses = [(int(elem), offset) for offset, elem in enumerate(elements[1].split(',')) if elem != 'x']
	ans = buses[0][0]
	acc = 1

	for bus in buses:
		ans = find(ans, bus[0], bus[1], acc)
		acc *= bus[0]

	return ans

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 13 : Shuttle Search - part 2')
	print(f'>>> Answer : {solution(inputs)}')