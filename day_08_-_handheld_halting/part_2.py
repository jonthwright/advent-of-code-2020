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
			if self.eip == len(self.prog):
				return 0

def solution(elements):
	cons = console(elements)
	cons.run()

	for i in range(len(elements)):
		if 'acc' in elements[i]:
			continue
		elif 'jmp' in elements[i]:
			mod = elements[i].replace('jmp', 'nop')
		elif 'nop' in elements[i]:
			mod = elements[i].replace('nop', 'jmp')
		else:
			raise ValueError(f'Invalid op code: [{cons.eip}] {cons.prog}')
		
		cons = console(elements[:i] + [mod] + elements[i + 1:])
		if cons.run() == 0:
			return cons.acc

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.read().strip().splitlines()
	print(f'Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()