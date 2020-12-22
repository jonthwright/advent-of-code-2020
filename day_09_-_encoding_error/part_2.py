#!/usr/bin/env python3

def valid_number(window, number):
	for n in window:
		dif = abs(number - n)
		if n != dif and dif in window:
			return True
	return False


def find_wrong(elements, window_size):
	window = elements[:window_size]
	for i, number in enumerate(elements[window_size:], 1):
		if not valid_number(window, number): 
			return number
		window = elements[i:window_size + i]
	return False

def solution(elements):
	WIN_SIZE = 25
	wrong = find_wrong(elements, WIN_SIZE)
	
	for size in range(2, len(elements)):
		window = elements[:size]

		for i in range(1, len(elements) - size):
			if sum(window) == wrong: 
				return min(window) + max(window)
			window = elements[i:size + i]
	return False

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [int(e.strip('\n')) for e in f.readlines()]
	print(f'Answer : {solution(inputs)}')