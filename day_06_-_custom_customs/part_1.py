#!/usr/bin/env python3

def solution(elements):
	return sum(len(set(ele.replace('\n', ''))) for ele in elements)

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split('\n\n')
	print(f'Answer : {solution(inputs)}')