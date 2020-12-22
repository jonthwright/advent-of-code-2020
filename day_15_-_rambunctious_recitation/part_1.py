#!/usr/bin/env python3

from collections import defaultdict

def solution(elements):
	nums = defaultdict(list)

	for i, n in enumerate(elements):
		nums[n].append(i)

	last = n = elements[-1]

	for i in range(len(elements), 2020):
		if len(nums[last]) < 2:
			last = 0
			nums[0].append(i)
		else:
			last = nums[last][-1] - nums[last][-2]
			nums[last].append(i)

	return last

if __name__ == '__main__':
	inputs = [0, 12, 6, 13, 20, 1, 17]
	print(f'Answer : {solution(inputs)}')