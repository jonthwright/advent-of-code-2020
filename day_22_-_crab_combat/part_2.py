#!/usr/bin/env python3

def stringify(lst):
    return ','.join(str(e) for e in lst)

def calculate_score(winning_deck):
	descending_scores = sorted(winning_deck, reverse=True)
	return sum(x * y for x, y in zip(winning_deck, descending_scores))

def combat(player_one_deck, player_two_deck):
	states = set()

	while player_one_deck and player_two_deck:
		winner = None

		state = f'{stringify(player_one_deck)}|{stringify(player_two_deck)}'

		if state in states:
			return (1, player_one_deck)
		states.add(state)

		player_one_card, player_two_card = player_one_deck.pop(0), player_two_deck.pop(0)

		if len(player_one_deck) >= player_one_card and len(player_two_deck) >= player_two_card:
			winner, _ = combat(player_one_deck[:player_one_card], player_two_deck[:player_two_card])
		else:
			winner = 1 if player_one_card > player_two_card else 2

		if winner == 1:
			player_one_deck.extend([player_one_card, player_two_card])
		else:
			player_two_deck.extend([player_two_card, player_one_card])
	
	deck_winner = 1 if player_one_deck else 2
	winning_deck = player_one_deck if player_one_deck else player_two_deck

	return (deck_winner, winning_deck)

def solution(elements):
	player_one_deck, player_two_deck = elements
	_, winning_deck = combat(player_one_deck, player_two_deck)
	return calculate_score(winning_deck)

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [[int(line) for line in lines.splitlines() if line.isnumeric()] for lines in f.read().split('\n\n')]
	print(f'Answer : {solution(inputs)}')