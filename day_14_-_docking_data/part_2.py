#!/usr/bin/env python3

def get_indexes(mask):
	if 'X' in mask:
		x = mask.index('X')
		return get_indexes(mask[:x] + '0' + mask[x + 1 :]) + get_indexes(mask[:x] + '1' + mask[x + 1 :])
	return [int(mask, 2)]

def solution(elements):
	mem = {}
	mask = None

	for inst in elements:
		if inst.startswith('mask'):
			mask = inst.split(' ')[2]
		elif inst.startswith('mem'):
			idx = int(inst.split('[')[1].split(']')[0])
			val = int(inst.split(' ')[2])
			idx_mask = ''

			for m, i in zip(mask, f'{idx:036b}'):
				if m == '0':
					idx_mask += i
				elif m == '1' or m == 'X':
					idx_mask += m
				else:
					assert False

			idxs = get_indexes(idx_mask)

			for idx in idxs:
				mem[idx] = val
	
	return sum(mem.values())

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 14 : Docking Data - part 2')
	print(f'>>> Answer : {solution(inputs)}')