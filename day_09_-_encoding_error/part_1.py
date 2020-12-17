def valid_number(window, number):
	for n in window:
		dif = abs(number - n)
		if n != dif and dif in window:
			return True
	return False

def solution(inputs):
	WIN_SIZE = 25
	window = inputs[:WIN_SIZE]

	for i, number in enumerate(inputs[WIN_SIZE:], 1):
		if not valid_number(window, number): 
			return number
		window = inputs[i:WIN_SIZE+i]
	return False

def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(e) for e in f.read().strip().splitlines()]
	print(solution(inputs))

if __name__ == '__main__':
	main()