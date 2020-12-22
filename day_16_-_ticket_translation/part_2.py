#!/usr/bin/env python3

import re

def is_valid_field(rules, i):
	return any([v[0] <= i <= v[1] or v[2] <= i <= v[3] for v in rules.values()])

def reduce(fn, lst, acc):
	for e in lst:
		acc = fn(e, acc)
	return acc

def product(array, acc=1):
	return reduce(lambda x, y: x * y, array, acc)

def solution(elements):
	rules_raw, myticket_raw, others_raw = elements
	others = [list(map(int, o.split(','))) for o in others_raw[1:]]
	myticket = list(map(int, myticket_raw[1].split(',')))

	rules = {}
	possibles = {}
	matched = {}

	for rule in rules_raw:
		search = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', rule)
		name = search.group(1)
		nums = list(map(int, search.groups()[1:]))
		rules[name] = nums

	valid_others = [other for other in others if all([is_valid_field(rules, o) for o in other])]

	for name, bounds in rules.items():
		possibles[name] = [i for i in range(len(rules)) if all([is_valid_field({name: bounds}, t[i]) for t in valid_others])]

	for name, possibilities in sorted(possibles.items(), key=lambda x: len(x[1])):
		index = [i for i in possibilities if i not in matched]
		matched[index[0]] = name

	deps = [x for i, x in enumerate(myticket) if 'departure' in matched[i]]
	deps_prod = product(deps)

	return deps_prod

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [x.split('\n') for x in f.read().split('\n\n')]
	print('Day 16 : Ticket Translation - part 2')
	print(f'>>> Answer : {solution(inputs)}')