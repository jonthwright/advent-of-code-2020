#!/usr/bin/env python3

import re

def is_valid_field(rules, i):
	return any([v[0] <= i <= v[1] or v[2] <= i <= v[3] for v in rules.values()])

def solution(elements):
	rules_raw, _, others_raw = inputs

	rules = {}
	for rule in rules_raw:
		search = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', rule)
		name = search.group(1)
		nums = list(map(int, search.groups()[1:]))
		rules[name] = nums

	others = [list(map(int, o.split(','))) for o in others_raw[1:]]

	error_rate = sum(o for other in others for o in other if not is_valid_field(rules, o))

	return error_rate

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [x.split('\n') for x in f.read().split('\n\n')]
	print(f'Answer : {solution(inputs)}')