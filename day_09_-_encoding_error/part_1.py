def valid_number(window, number):
	for n in window:
		dif = abs(number - n)
		if n != dif and dif in window:
			return True
	return False

def solution(elements):
	WIN_SIZE = 25
	window = elements[:WIN_SIZE]

	for i, number in enumerate(elements[WIN_SIZE:], 1):
		if not valid_number(window, number): 
			return number
		window = elements[i:WIN_SIZE+i]
	return False

def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(e) for e in f.read().strip().splitlines()]
	print(f'Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()