def solution(elements):
	start = int(elements[0])
	buses = [int(bus) for bus in elements[1].split(',') if bus != 'x']
	
	waits = [(bus, bus - (start % bus)) for bus in buses]
	target_bus = min(waits, key=lambda x: x[1])

	return target_bus[0] * target_bus[1]

def main():	
	with open('input_file.txt', 'r') as f:
		inputs = [e for e in f.read().strip().splitlines()]
	print(solution(inputs))

if __name__ == '__main__':
	main()