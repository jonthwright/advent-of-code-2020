import re

def solution(elements):
	convert = lambda x : x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
	elements = set(convert(e) for e in elements)
	return max(int(s, 2) for s in elements)

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split()
	print(solution(inputs))

if __name__ == '__main__':
	main()