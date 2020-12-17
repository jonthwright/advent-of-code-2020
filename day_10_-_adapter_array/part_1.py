def diff(x):
	return x[0] - x[1]

def solution(inputs):
	inputs.append(0)
	inputs.append(max(inputs) + 3)
	inputs.sort()
	diffs = list(map(diff, zip(inputs[1:], inputs[:-1])))
	one_diffs = diffs.count(1)
	three_diffs = diffs.count(3)
	return one_diffs * three_diffs

def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(e) for e in f.read().strip().splitlines()]
	print(solution(inputs))

if __name__ == '__main__':
	main()