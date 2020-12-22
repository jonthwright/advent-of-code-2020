#!/usr/bin/env python3

import re

def regex_builder(rules, r='0', depth=15):
	if depth == 0:
		return ''

	if rules[r][0][0].startswith('"'):
		return rules[r][0][0].strip('"')

	return '(' + '|'.join([''.join(regex_builder(rules, r=sub, depth=depth-1) for sub in subrule) for subrule in rules[r]]) + ')'

def solution(elements):
	rules_raw, msgs = elements

	rules = {}

	for rule in rules_raw.split('\n'):
		num, r = rule.split(': ')
		rules[num] = [s.split() for s in r.split(' | ')]
	
	rules['8'] = [['42'], ['42', '8']]
	rules['11'] = [['42', '31'], ['42', '11', '31']]

	regex = re.compile(regex_builder(rules))
	res = [regex.fullmatch(msg) for msg in msgs.split("\n")]
	
	return len([x for x in res if x])

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split("\n\n")
	print('Day 19 : Monster Messages - part 2')
	print(f'>>> Answer : {solution(inputs)}')