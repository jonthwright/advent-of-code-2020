#!/usr/bin/env python3

def evaluate(equation):
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
		total = int(eq[0])

		for i in range(1, len(eq), 2):
			total = eval(f'{total} {eq[i]} {eq[i+1]}')

		return total
	
def solution(elements):
	return sum(evaluate(eq) for eq in elements)
	
if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [x.strip('\n') for x in f.readlines()]
	print(f'Answer : {solution(inputs)}')