class console:
	def __init__(self, puzzle_input):
		self.acc = 0
		self.prog = [(line.split(' ')[0], int(line.split(' ')[1])) for line in puzzle_input]
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

def solution(inputs):
	cons = console(inputs)
	cons.run()
	return cons.acc

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.read().strip().splitlines()
	print(solution(inputs))

if __name__ == '__main__':
	main()