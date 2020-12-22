#!/usr/bin/env python3

def calculate_score(winning_deck):
	descending_scores = sorted(winning_deck, reverse=True)
	return sum(x * y for x, y in zip(winning_deck, descending_scores))

def solution(elements):
	player_one_deck, player_two_deck = elements

	while player_one_deck and player_two_deck:
		player_one_card, player_two_card = player_one_deck.pop(0), player_two_deck.pop(0)

		if player_one_card > player_two_card:
			player_one_deck.extend([player_one_card, player_two_card])
		elif player_one_card < player_two_card:
			player_two_deck.extend([player_two_card, player_one_card])
	
	score = calculate_score(player_one_deck if player_one_deck else player_two_deck)

	return score

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [[int(line) for line in lines.splitlines() if line.isnumeric()] for lines in f.read().split('\n\n')]
	print('Day 22 : Combat Crab - part 1')
	print(f'>>> Answer : {solution(inputs)}')