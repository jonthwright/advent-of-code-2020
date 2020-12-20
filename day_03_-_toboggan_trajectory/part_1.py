def solution(elements):
	slopeX, slopeY = 3, 1
	col = 0
	trees = 0

	for row in range(len(elements)):
		trees += elements[row][col % len(elements[0])] == '#'
		col += 3

	return trees

def process_inputs(inputs):
	return [list(inp.strip()) for inp in inputs]

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
	processed = process_inputs(inputs)
	print(f'Answer : {solution(processed)}')

if __name__ == '__main__':
	main()