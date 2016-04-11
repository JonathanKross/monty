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

def random_winner_door():

    return random.randint(1, 3)


def random_initial_door():

    return random.randint(1, 3)


def randomly_remove_eligible_door(winner_door, initial_door):

    removable_door = []

    for door in [1, 2, 3]:
        if door != winner_door and door != initial_door:
            removable_door.append(door)

    randomly_removed_door = random.choice(removable_door)

    return randomly_removed_door


def determine_winner_no_door_change(winner_door, initial_door):

    if initial_door == winner_door:
        return True
    else:
        return False


def always_switch_doors(initial_door, randomly_removed_door):

    switched_door = 0

    for door in [1, 2, 3]:
        if door != initial_door and door != randomly_removed_door:
            switched_door = door

    return switched_door

def determine_winner_door_change(winner_door, switched_door):

    if switched_door == winner_door:
        return True
    else:
        return False

def play_no_switch():
    winner_door = random_winner_door()
    intial_door = random_initial_door()
    determine_winner_no_door_change(winner_door, initial_door)


def play_switch():
    winner_door = random_winner_door()
    intial_door = random_initial_door()
    randomly_removed_door = randomly_remove_eligible_door(winner_door, initial_door)
    switched_door = always_switch_doors(initial_door, randomly_removed_door)
    determine_winner_no_door_change(winner_door, switched_door)
