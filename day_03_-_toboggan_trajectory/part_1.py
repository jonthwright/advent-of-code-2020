import re

def solution(elements):
    slopeX, slopeY = 3, 1
    row, col = 0, 0
    trees = 0

    while row < len(elements) - 1:
        
        col += 3
        row += 1
        
        trees += elements[row][col % len(elements[0])] == '#'

    return trees
def process_inputs(inputs):
    return [list(inp.strip()) for inp in inputs]

def main():
    with open('input_file.txt', 'r') as f:
        inputs = f.readlines()
        proccesed = process_inputs(inputs)
        print(solution(proccesed))

if __name__ == '__main__':
    main()