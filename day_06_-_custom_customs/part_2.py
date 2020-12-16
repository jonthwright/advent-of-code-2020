import string

def solution(elements):
	count = 0
	
	for elem in elements:
		ind_elem = elem.split("\n")
		for c in string.ascii_lowercase:
			count += all([c in a for a in ind_elem])
	
	return count

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split('\n\n')
	print(inputs[0])
	print(solution(inputs))

if __name__ == '__main__':
	main()