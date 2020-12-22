#!/usr/bin/env python3

from utils import advent
from collections import deque

def score(deck):
	return sum(i * c for i, c in enumerate(reversed(deck), 1))

def play(deck1, deck2):
	while deck1 and deck2:
		c1, c2 = deck1.popleft(), deck2.popleft()

		if c1 > c2:
			deck1.extend((c1, c2))
		else:
			deck2.extend((c2, c1))

	return deck1 if deck1 else deck2

def recursive_play(deck1, deck2):
	seen = set()

	while deck1 and deck2:
		k = (tuple(deck1), tuple(deck2))
		if k in seen:
			return 1, deck1

		seen.add(k)
		c1, c2 = deck1.popleft(), deck2.popleft()

		if len(deck1) >= c1 and len(deck2) >= c2:
			sub1, sub2 = list(deck1)[:c1], list(deck2)[:c2]
			winner, _ = recursive_play(deque(sub1), deque(sub2))
		else:
			winner = 1 if c1 > c2 else 2

		if winner == 1:
			deck1.extend((c1, c2))
		else:
			deck2.extend((c2, c1))

	return (1, deck1) if deck1 else (2, deck2)


advent.setup(2020, 22)
fin = advent.get_input()

deck1, deck2 = map(str.splitlines, fin.read().split('\n\n'))
deck1 = deque(map(int, deck1[1:]))
deck2 = deque(map(int, deck2[1:]))

winner_deck  = play(deck1.copy(), deck2.copy())
winner_score = score(winner_deck)
advent.print_answer(1, winner_score)

_, winner_deck = recursive_play(deck1, deck2)
winner_score   = score(winner_deck)
advent.print_answer(2, winner_score)
