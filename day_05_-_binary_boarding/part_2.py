import re

def solution(elements):
	convert = lambda x : x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
	claimed = set(int(convert(e), 2) for e in elements)
	available = set(range(128 * 8))
	open_seats = available - claimed

	seat = [seat for seat in open_seats
				if seat + 1 not in open_seats and seat - 1 not in open_seats][0]

	return seat

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
	print(solution(inputs))

if __name__ == '__main__':
	main()