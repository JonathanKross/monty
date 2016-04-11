import random


def num_doors():

    num_doors = int(input("How many doors do you want to test? "))
    return num_doors

def random_winner_door(num_doors):

    return random.randint(1, num_doors)


def random_initial_door(num_doors):

    return random.randint(1, num_doors)


def determine_winner_no_door_change(winner_door, initial_door):

    if initial_door == winner_door:
        return True
    else:
        return False


def play_no_switch(num_doors):
    winner_door = random_winner_door(num_doors)
    initial_door = random_initial_door(num_doors)
    end_result_no_switch = determine_winner_no_door_change(winner_door, initial_door)
    return end_result_no_switch


def randomly_remove_eligible_door(winner_door, initial_door, num_doors):

    removable_door = []

    for door in list(range(1, num_doors + 1)):
        if door != winner_door and door != initial_door:
            removable_door.append(door)

    randomly_removed_door = random.choice(removable_door)

    return randomly_removed_door


def always_switch_doors(initial_door, randomly_removed_door, num_doors):

    switchable_door = []

    for door in list(range(1, num_doors + 1)):
        if door != initial_door and door != randomly_removed_door:
            switchable_door.append(door)

    switched_door = random.choice(switchable_door)

    return switched_door

def determine_winner_door_change(winner_door, switched_door):

    if switched_door == winner_door:
        return True
    else:
        return False


def play_switch(num_doors):
    winner_door = random_winner_door(num_doors)
    initial_door = random_initial_door(num_doors)
    randomly_removed_door = randomly_remove_eligible_door(winner_door, initial_door, num_doors)
    switched_door = always_switch_doors(initial_door, randomly_removed_door, num_doors)
    end_result_switch = determine_winner_door_change(winner_door, switched_door)
    return end_result_switch



def simulate_no_switch(num_doors, simulations):
    no_switch_wins = 0
    counter = 0

    while counter < simulations:
        counter += 1
        if play_no_switch(num_doors) == True:
            no_switch_wins += 1

    return no_switch_wins


def simulate_switch(num_doors, simulations):
    switch_wins = 0
    counter = 0

    while counter < simulations:
        counter += 1
        if play_switch(num_doors) == True:
            switch_wins += 1

    return switch_wins



def main():

    test_num_doors = num_doors()
    simulations = int(input("How many simulations would you like to run? "))
    no_switch_wins = simulate_no_switch(test_num_doors, simulations)
    switch_wins = simulate_switch(test_num_doors, simulations)

    print("No switch win percentage: {}%".format(round((no_switch_wins/simulations) * 100), 2))
    print("Switch win percentage: {}%".format(round((switch_wins/simulations) * 100), 2))


if __name__ == '__main__':
    main()
