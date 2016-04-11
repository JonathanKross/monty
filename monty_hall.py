import random


def random_winner_door():

    return random.randint(1, 3)


def random_initial_door():

    return random.randint(1, 3)


def determine_winner_no_door_change(winner_door, initial_door):

    if initial_door == winner_door:
        return True
    else:
        return False


def play_no_switch():
    winner_door = random_winner_door()
    initial_door = random_initial_door()
    end_result_no_switch = determine_winner_no_door_change(winner_door, initial_door)
    return end_result_no_switch


def randomly_remove_eligible_door(winner_door, initial_door):

    removable_door = []

    for door in [1, 2, 3]:
        if door != winner_door and door != initial_door:
            removable_door.append(door)

    randomly_removed_door = random.choice(removable_door)

    return randomly_removed_door


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


def play_switch():
    winner_door = random_winner_door()
    initial_door = random_initial_door()
    randomly_removed_door = randomly_remove_eligible_door(winner_door, initial_door)
    switched_door = always_switch_doors(initial_door, randomly_removed_door)
    end_result_switch = determine_winner_door_change(winner_door, switched_door)
    return end_result_switch



def simulate_no_switch(simulations):
    no_switch_wins = 0
    counter = 0

    while counter < simulations:
        counter += 1
        if play_no_switch() == True:
            no_switch_wins += 1

    return no_switch_wins


def simulate_switch(simulations):
    switch_wins = 0
    counter = 0

    while counter < simulations:
        counter += 1
        if play_switch() == True:
            switch_wins += 1

    return switch_wins

    

def main():

    simulations = int(input("How many simulations would you like to run? "))
    no_switch_wins = simulate_no_switch(simulations)
    switch_wins = simulate_switch(simulations)

    print("No switch win percentage: {}%".format(round((no_switch_wins/1000.0) * 100), 2))
    print("Switch win percentage: {}%".format(round((switch_wins/1000.0) * 100), 2))


if __name__ == '__main__':
    main()
