def valid_number(window, number):
	for n in window:
		dif = abs(number - n)
		if n != dif and dif in window:
			return True
	return False


def find_wrong(inputs, window_size):
	window = inputs[:window_size]
	for i, number in enumerate(inputs[window_size:], 1):
		if not valid_number(window, number): 
			return number
		window = inputs[i:window_size + i]
	return False

def solution(inputs):
	WIN_SIZE = 25
	wrong = find_wrong(inputs, WIN_SIZE)
	
	for size in range(2, len(inputs)):
		window = inputs[:size]

		for i in range(1, len(inputs) - size):
			if sum(window) == wrong: 
				return min(window) + max(window)
			window = inputs[i:size + i]
	return False

def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(e) for e in f.read().strip().splitlines()]
	print(solution(inputs))

if __name__ == '__main__':
	main()