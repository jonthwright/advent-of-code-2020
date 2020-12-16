import re

def count_bags(bag_type, bags):
    return 1 + sum(int(number) * count_bags(colour, bags) for number, colour in bags[bag_type])

def solution(inputs):
	bags = {}

	for line in inputs:
		colour = re.match(r"(.+?) bags contain", line)[1]  
		bags[colour] = re.findall(r"(\d+?) (.+?) bags?", line)

	return count_bags("shiny gold", bags) - 1

def main():
	with open('input_file.txt', 'r') as f:
		inputs = f.readlines()
		inputs = [l.strip('\n') for l in inputs]
	print(solution(inputs))

if __name__ == '__main__':
	main()