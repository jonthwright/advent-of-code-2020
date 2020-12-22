#!/usr/bin/env python3

def evaluate(equation, operators='+*'):
	if '(' in equation:
		open_paren = 0
		i = 0
		start = equation.index('(')

		for i in range(start, len(equation)):
			if equation[i] == '(':
				open_paren += 1
			elif equation[i] == ')':
				open_paren -= 1
			
			if open_paren == 0:
				break

		return evaluate(equation[:start] + str(evaluate(equation[start + 1 : i])) + equation[i + 1 :])
	else:
		eq = equation.split(' ')

		for op in operators:
			i = 1

			while i < len(eq):
				if eq[i] in op:
					eq = eq[: i - 1] + [str(eval(" ".join(eq[i - 1 : i + 2])))] + eq[i + 2 :]
				else:
					i += 2

		return int(eq[0])

	
def solution(elements):
	return sum(int(evaluate(eq)) for eq in elements)
	
if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [x.strip('\n') for x in f.readlines()]
	print('Day 18 : Operation Order - part 2')
	print(f'>>> Answer : {solution(inputs)}')