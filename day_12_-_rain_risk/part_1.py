import math

def solution(elements):
	direction = 90
	x, y = 0, 0
	
	for cmd in elements:
		instruction, units = cmd[0], int(cmd[1:	])
		if instruction == 'N':
			y += units
		elif instruction == 'S':
			y -= units
		elif instruction == 'E':
			x += units
		elif instruction == 'W':
			x -= units
		elif instruction == 'L':
			direction -= units
			direction %= 360
		elif instruction == 'R':
			direction += units
			direction %= 360
		elif instruction == 'F':
			x += round(math.sin(math.radians(direction)) * units)
			y += round(math.cos(math.radians(direction)) * units)

	return abs(x) + abs(y)

def main():	
	with open('input_file.txt', 'r') as f:
		inputs = [e for e in f.read().strip().splitlines()]
	print(f'Answer : {solution(inputs)}')

if __name__ == '__main__':
	main()