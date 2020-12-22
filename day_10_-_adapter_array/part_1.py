#!/usr/bin/env python3

def diff(x):
	return x[0] - x[1]

def solution(elements):
	jolts = sorted(elements)
	jolts.append(jolts[-1] + 3)

	last_jolt = 0
	diffs = [0, 0, 0, 0]

	for jolt in jolts:
		diffs[jolt - last_jolt] += 1
		last_jolt = jolt

	return diffs[1] * diffs[3]

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [int(e.strip('\n')) for e in f.readlines()]
	print('Day 10 : Adapter Array - part 1')
	print(f'>>> Answer : {solution(inputs)}')