import math
import random


'''
Door One
Door Two
Door Three

Randomly put goat in 1, 2, or 3
Randomly choose a door
Randomly remove an eligible door
Always stay with initial door
Find if win

Randomly put goat in 1, 2, or 3
Randomly choose a door
Always switch door
Find if win

'''


winner_door = random.randint(1, 3)
initial_door = random.randint(1, 3)

removable_door = []
for door in [1, 2, 3]:
    if door != winner_door:
        removable_door.append(door)

randomly_removed_door = random.choice(removable_door)

if initial_door == winner_door:
    print("WINNER")
else:
    print("LOSER")
