def solution(elements):
	return sum(len(set(ele.replace('\n', ''))) for ele in elements)

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.read().split('\n\n')
	print(solution(inputs))

if __name__ == '__main__':
	main()