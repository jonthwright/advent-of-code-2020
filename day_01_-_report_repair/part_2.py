def solution(elements):
	elements.sort()
	
	for i in range(len(elements) - 2):
		if i > 0 and elements[i] == elements[i-1]:
			continue
		l = i + 1
		r = len(elements) - 1
		
		while (l < r):
			sum = elements[i] + elements[l] + elements[r]
			if sum < 2020:
				l += 1
			elif sum > 2020:
				r -= 1
			else:
				return elements[i] * elements[l] * elements[r]
	return -1

def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readlines()]
	print(f'Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()