from collections import Counter

def solution(inputs):
	jolts = sorted(inputs)
	jolts.append(jolts[-1] + 3)

	dp = Counter()
	dp[0] = 1

	for jolt in jolts:
		dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]

	return dp[jolts[-1]]

def main():
	with open('input_file.txt', 'r') as f:
		inputs = [int(e) for e in f.read().strip().splitlines()]
	print(solution(inputs))

if __name__ == '__main__':
	main()