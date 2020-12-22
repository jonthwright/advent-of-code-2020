#!/usr/bin/env python3

def solution(elements):
	return sum(len(set(ele.replace('\n', ''))) for ele in elements)

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split('\n\n')
	print('Day 06 : Custom Customs - part 1')
	print(f'>>> Answer : {solution(inputs)}')