#!/usr/bin/env python3

class console:
	def __init__(self, inputs):
		self.acc = 0
		self.prog = [(line.split(' ')[0], int(line.split(' ')[1])) for line in inputs]
		self.eip = 0
		self.executed_insts = set()

	def run(self):
		while self.eip not in self.executed_insts:
			self.executed_insts.add(self.eip)
			op, arg = self.prog[self.eip]
			if op == 'acc':
				self.acc += arg
				self.eip += 1
			elif op == 'jmp':
				self.eip += arg
			elif op == 'nop':
				self.eip += 1
			else:
				raise ValueError(f'Invalid op code: [{self.eip}] {self.prog}')

def solution(elements):
	cons = console(elements)
	cons.run()
	return cons.acc

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [e.strip('\n') for e in f.readlines()]
	print('Day 08 : Handheld Halting - part 1')
	print(f'>>> Answer : {solution(inputs)}')