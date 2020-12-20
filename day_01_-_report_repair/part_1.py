def solution(elements):
	complements = {}
	
	for elem in elements:
		comp = 2020 - elem
		if comp in elements:
			return elem * comp
	return -1

def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readlines()]
	print(f'Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()