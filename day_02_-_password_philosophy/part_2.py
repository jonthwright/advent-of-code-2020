import re

def solution(elements):
	valid = 0

	for (i, j, ltr, password) in elements:
		valid += (password[i - 1] == ltr) ^ (password[j - 1] == ltr)
	
	return valid

def process_inputs(inputs):
	output = []
	for i in inputs:
		regex = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', i)
		output.append((int(regex.group(1)), int(regex.group(2)), regex.group(3), regex.group(4)))
	return output

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
		processed = process_inputs(inputs)
		print(solution(processed))

if __name__ == '__main__':
	main()