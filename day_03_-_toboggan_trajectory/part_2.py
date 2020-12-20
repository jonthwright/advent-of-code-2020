def solution(elements):
	total = 1
	for change_col, change_row in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
		col = 0
		trees = 0

		for r in range(0,len(elements),change_row):            
			trees += elements[r][col % len(elements[0])] == '#'
			col += change_col

		total *= trees

	return total

def process_inputs(inputs):
	return [list(inp.strip()) for inp in inputs]

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
	processed = process_inputs(inputs)
	print(f'Answer : {solution(processed)}')

if __name__ == '__main__':
	main()