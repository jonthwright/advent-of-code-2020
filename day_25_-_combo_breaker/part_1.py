#!/usr/bin/env python3

def find_secret_loop(pk_one, pk_two):
    pass

def solution(card_public_key, door_public_key):
	subject, mod = 7, 20201227
	value, secret_loop = 1, 1
	while (value := (value * subject) % mod) != card_public_key:
		secret_loop += 1
	return pow(door_public_key, secret_loop, mod)

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [int(line) for line in f.readlines()]
	print('Day 25 : Code Breaker - part 1')
	print(f'>>> Answer : {solution(*inputs)}')