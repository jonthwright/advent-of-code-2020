#!/usr/bin/env python3

def solution(elements):
	mem = {}
	m_and, m_or = None, None

	for inst in elements:
		if inst.startswith('mask'):
			mask_in = inst.split(' ')[2]
			m_or = int(mask_in.replace('X', '0'), 2)
			m_and = int(mask_in.replace('X', '1'), 2)
		elif inst.startswith('mem'):
			idx = int(inst.split('[')[1].split(']')[0])
			val = int(inst.split(' ')[2])
			mem[idx] = (val & m_and) | m_or

	return sum(mem.values())

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 14 : Docking Data - part 1')
	print(f'>>> Answer : {solution(inputs)}')