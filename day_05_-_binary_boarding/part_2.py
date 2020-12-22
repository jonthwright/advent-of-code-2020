#!/usr/bin/env python3

def solution(elements):
	convert = lambda x : x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
	claimed = set(int(convert(e), 2) for e in elements)
	available = set(range(128 * 8))
	open_seats = available - claimed

	seat = [seat for seat in open_seats
				if seat + 1 not in open_seats and seat - 1 not in open_seats]

	return seat[0]

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 05 : Binary Boarding - part 2')
	print(f'>>> Answer : {solution(inputs)}')