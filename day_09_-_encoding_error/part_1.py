#!/usr/bin/env python3

def valid_number(window, number):
	for n in window:
		dif = abs(number - n)
		if n != dif and dif in window:
			return True
	return False

def solution(elements):
	WIN_SIZE = 25
	window = elements[:WIN_SIZE]

	for i, number in enumerate(elements[WIN_SIZE:], 1):
		if not valid_number(window, number): 
			return number
		window = elements[i:WIN_SIZE+i]
	return False


if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [int(e.strip('\n')) for e in f.readlines()]
	print('Day 09 : Encoding Error - part 1')
	print(f'>>> Answer : {solution(inputs)}')