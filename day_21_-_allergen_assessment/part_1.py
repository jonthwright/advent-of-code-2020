#!/usr/bin/env python3

import re

def solution(elements):
	allergens_ingredients, ingredient_counter= {}, {}
	all_ingredients = set()

	for elem in elements:
		ingredients, allergens = [re.split(r'[\s,]+', e) for e in elem.replace(')', '').split(' (contains ')]
		for allergen in allergens:
			if allergen in allergens_ingredients:
				allergens_ingredients[allergen] = set(i for i in ingredients if i in allergens_ingredients[allergen])
			else:
				allergens_ingredients[allergen] = set(ingredients)

		for ingredient in ingredients:
			if ingredient not in ingredient_counter:
				ingredient_counter[ingredient] = 0
			ingredient_counter[ingredient] += 1
			all_ingredients.add(ingredient)

	defined_allergens, defined_ingredients = {}, {}
	keys = list(allergens_ingredients.keys())
	
	while keys:
		defined = [k for k, v in allergens_ingredients.items() if len(v) == 1][0]
		ingredient = allergens_ingredients[defined].pop()
		defined_allergens[defined] = ingredient
		del allergens_ingredients[defined]

		for a in allergens_ingredients:
			if ingredient in allergens_ingredients[a]:
				allergens_ingredients[a].remove(ingredient)

		keys = list(allergens_ingredients.keys())
	
	for k, v in defined_allergens.items():
		defined_ingredients[v] = k

	ok_ingredients = [ingredient_counter[ingre] for ingre in all_ingredients if ingre not in defined_ingredients]
	
	return sum(ok_ingredients)

if __name__ == '__main__':
	with open('input_file.txt', 'r') as f:
		inputs = [line.strip('\n') for line in f.readlines()]
	print('Day 21 : Allergen Assessment - part 1')
	print(f'>>> Answer : {solution(inputs)}')