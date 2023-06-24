"""
Escape or ELSE

Author: Thomas Tarango
Date: 6/24/2024
"""

import random
from time import sleep

print('███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗     ██████╗ ██████╗     ███████╗██╗     ███████╗███████╗')
sleep(0.05)
print('██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝    ██╔═══██╗██╔══██╗    ██╔════╝██║     ██╔════╝██╔════╝')
sleep(0.05)
print('█████╗  ███████╗██║     ███████║██████╔╝█████╗      ██║   ██║██████╔╝    █████╗  ██║     ███████╗█████╗  ')
sleep(0.05)
print('██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝      ██║   ██║██╔══██╗    ██╔══╝  ██║     ╚════██║██╔══╝  ')
sleep(0.05)
print('███████╗███████║╚██████╗██║  ██║██║     ███████╗    ╚██████╔╝██║  ██║    ███████╗███████╗███████║███████╗')
sleep(0.05)
print('╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝     ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚══════╝╚══════╝')
sleep(0.05)
print('by Thomas Tarango')
sleep(3)


# Game Instructions
def show_instructions():
    print("\nYou are in your house.")
    sleep(2)
    print("Collect all items without mother noticing.")
    sleep(2)
    print("Move to any connected room by typing 'go' followed by the direction (north, south, east, or west).")
    sleep(3)
    print("Pick up items in the room by typing 'get' followed by the name of the item.")
    sleep(2)
    print("If mother is in the same room, you'll have to roll a die to hide or escape.")
    sleep(2)
    print("If you're caught, game over!\n")
    sleep(2)


# Player's Current Status
def get_status(current_room, inventory, mother_room):
    print("-----------------------------")
    print("You are in the", current_room)
    sleep(1)
    if mother_room == current_room:
        print("Mother is in the room with you!")
        sleep(1)
    else:
        connected_rooms = [room for room in rooms[current_room].values() if room != "items"]
        if mother_room in connected_rooms:
            print(f"You hear Mother's hums coming from {mother_room}.")
            sleep(1)
    print("Inventory:", ', '.join(inventory))
    sleep(1)
    if rooms[current_room]["items"]:
        print("You see:", ', '.join(rooms[current_room]["items"]))
        sleep(1)
    else:
        print("There's nothing to collect here.")
        sleep(1)
    for direction, room in rooms[current_room].items():
        if direction != "items":
            print(f"Go {direction.capitalize()} to enter {room}")
            sleep(1)
    print("-----------------------------")


# Dice Roll
def roll_dice(player_inventory):
    return random.randint(1, 20) + len(player_inventory)


# Hide or Escape
def attempt_escape(player_inventory):
    while True:
        print('███▄ ▄███▓ ▒█████  ▄▄▄█████▓ ██░ ██ ▓█████  ██▀███')
        sleep(0.08)
        print('▓██▒▀█▀ ██▒▒██▒  ██▒▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒')
        sleep(0.07)
        print('▓██    ▓██░▒██░  ██▒▒ ▓██░ ▒░▒██▀▀██░▒███   ▓██ ░▄█ ▒')
        sleep(0.06)
        print('▒██    ▒██ ▒██   ██░░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄')
        sleep(0.05)
        print('▒██▒   ░██▒░ ████▓▒░  ▒██▒ ░ ░▓█▒░██▓░▒████▒░██▓ ▒██▒')
        sleep(0.04)
        print('░ ▒░   ░  ░░ ▒░▒░▒░   ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░')
        sleep(0.03)
        print('░  ░      ░  ░ ▒ ▒░     ░     ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░')
        sleep(0.02)
        print('░      ░   ░ ░ ░ ▒    ░       ░  ░░ ░   ░     ░░   ░')
        sleep(0.01)
        print()
        sleep(0.075)
        print('██░ ██  ▄▄▄        ██████')
        sleep(0.05)
        print('▓██░ ██▒▒████▄    ▒██    ▒')
        sleep(0.04)
        print('▒██▀▀██░▒██  ▀█▄  ░ ▓██▄')
        sleep(0.03)
        print('░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒')
        sleep(0.02)
        print('░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒')
        sleep(0.01)
        print('▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░')
        sleep(0.01)
        print('▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░')
        sleep(0.01)
        print('░  ░░ ░  ░   ▒   ░  ░  ░')
        sleep(0.01)
        print('░  ░  ░      ░  ░      ░')
        print()
        sleep(0.075)
        print('▓█████  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  ▓█████ ▓█████▄')
        sleep(0.09)
        print('▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌')
        sleep(0.08)
        print('▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▒███   ░██   █▌')
        sleep(0.07)
        print('▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌')
        sleep(0.06)
        print('░▒████▒▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒░▒████▒░▒████▓')
        sleep(0.05)
        print('░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒')
        sleep(0.04)
        print('░ ░  ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒')
        sleep(0.03)
        print('░      ░   ░ ░   ░         ░     ░░   ░    ░    ░ ░  ░')
        sleep(0.02)
        print('░  ░         ░             ░  ░   ░        ░  ░   ░')
        sleep(0.01)
        print('░')
        sleep(0.075)
        print('▄▄▄█████▓ ██░ ██ ▓█████')
        sleep(0.08)
        print('▓  ██▒ ▓▒▓██░ ██▒▓█   ▀')
        sleep(0.07)
        print('▒ ▓██░ ▒░▒██▀▀██░▒███')
        sleep(0.06)
        print('░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄')
        sleep(0.05)
        print('▒██▒ ░ ░▓█▒░██▓░▒████▒')
        sleep(0.04)
        print('▒ ░░    ▒ ░░▒░▒░░ ▒░ ░')
        sleep(0.03)
        print('░     ▒ ░▒░ ░ ░ ░  ░')
        sleep(0.02)
        print('░       ░  ░░ ░   ░')
        sleep(0.01)
        print('░  ░  ░   ░  ░')
        print()
        sleep(0.075)
        print('██▀███   ▒█████   ▒█████   ███▄ ▄███▓')
        sleep(0.08)
        print('▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒')
        sleep(0.07)
        print('▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▓██    ▓██░')
        sleep(0.06)
        print('▒██▀▀█▄  ▒██   ██░▒██   ██░▒██    ▒██')
        sleep(0.05)
        print('░██▓ ▒██▒░ ████▓▒░░ ████▓▒░▒██▒   ░██▒')
        sleep(0.04)
        print('░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░')
        sleep(0.03)
        print('░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░')
        sleep(0.02)
        print('░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░')
        sleep(0.01)
        print('░         ░ ░      ░ ░         ░')
        sleep(.5)

        action = input("Will you hide or escape? ").lower()
        if action not in ['hide', 'escape']:
            print("Invalid action. You can either 'hide' or 'escape'. "
                  "Try again.")
            sleep(1)
            continue

        bonus = len(player_inventory)
        player_roll = roll_dice(player_inventory) + bonus
        mother_roll = random.randint(1, 20)

        if bonus > 0:
            print(f"You rolled a {player_roll} (including a +{bonus} bonus "
                  f"for items collected). Mother rolled a {mother_roll}.")
            sleep(1)
        else:
            print(f"You rolled a {player_roll}. Mother rolled a {mother_roll}.")
            sleep(1)

        if player_roll > mother_roll:
            print(f"You successfully {action} from Mother!")
            sleep(1)
            return 'escaped' if action == 'escape' else True
        elif player_roll < mother_roll:
            print(f"You failed to {action}, Mother is suspicious but she's "
                  "distracted by Minnie, the family cat.")
            sleep(2)
            print("You have one more chance...")
            sleep(2)
            player_roll = roll_dice(player_inventory) + bonus
            mother_roll = random.randint(1, 20)

            if bonus > 0:
                print(f"You rolled a {player_roll} (including a +{bonus} bonus "
                      f"for items collected) on your second attempt. Mother "
                      f"rolled a {mother_roll}.")
            else:
                print(f"You rolled a {player_roll} on your second attempt. "
                      f"Mother rolled a {mother_roll}.")

            if player_roll > mother_roll:
                print(f"You successfully {action} on your second attempt!")
                sleep(2)
                return 'escaped' if action == 'escape' else True
            else:
                print("You're caught. Game Over.")
                sleep(2)
                return False
        else:
            print("It's a draw! Mother gets a call on her cell phone and "
                  "is momentarily distracted. You have another chance to "
                  f"{action}.")
            sleep(2)
            continue


# Move Mother
def move_mother(mother_room):
    possible_rooms = [rooms[mother_room][direction] for direction in rooms[mother_room] if direction != "items"]
    return random.choice(possible_rooms)


# Move Player
def go(player_room, direction):
    if direction in rooms[player_room]:
        return rooms[player_room][direction]
    else:
        print("You can't go that way.")
        return player_room


# Pick up Items
def get(player_room, player_inventory, item_name):
    item_found = False
    for item in rooms[player_room]["items"]:
        if item.lower() == item_name:
            player_inventory.append(item)
            rooms[player_room]["items"].remove(item)
            print("Got", item)
            item_found = True
            break
    if not item_found:
        print("Can't get", item_name)
    return player_inventory


# Escape to Connected Room
def escape_to(player_room):
    connected_rooms = [direction for direction, room in rooms[player_room].items() if direction != "items"]
    print("Escape to:")
    sleep(1)
    for direction in connected_rooms:
        print(f"- {direction.capitalize()} to enter {rooms[player_room][direction]}")
        sleep(0.1)
    while True:
        choice = input("Where do you want to escape to? ").lower()
        if choice in connected_rooms:
            return rooms[player_room][choice]
        else:
            print("Invalid choice. Try again.")
            sleep(1)


# Main Game Loop
def game():
    show_instructions()
    player_room = "Kitchen"
    player_inventory = []
    mother_room = "Mother's Bedroom"
    while True:
        if mother_room == player_room:
            result = attempt_escape(player_inventory)
            if result == 'escaped':
                player_room = escape_to(player_room)
            elif not result:
                break
        get_status(player_room, player_inventory, mother_room)
        command = input("> ").lower().split()
        if command[0] == 'go':
            player_room = go(player_room, command[1])
        elif command[0] == 'get':
            if len(command) > 1:
                player_inventory = get(player_room, player_inventory, ' '.join(command[1:]))
            else:
                print("Please provide the name of the item you want to get.")
        elif command[0] == 'escape':
            player_room = escape_to(player_room)
        else:
            print("Invalid command. Try again.")
            continue
        mother_room = move_mother(mother_room)
    print("Game Over.")


# Game Rooms and Items
rooms = {
    "Garage": {"east": "Laundry Room", "items": ["tools", "bike"]},
    "Laundry Room": {"south": "Kitchen", "west": "Garage", "items": ["clean clothes"]},
    "Living Room": {"east": "Kitchen", "items": ["scattered toys"]},
    "Kitchen": {"north": "Laundry Room", "east": "Living Room", "west": "Child's Bedroom", "items": ["dirty dishes"]},
    "Child's Bedroom": {"north": "Child's Study Room", "east": "Kitchen", "items": ["books", "dirty clothes"]},
    "Child's Study Room": {"south": "Child's Bedroom", "items": ["pens", "papers", "trash"]},
    "Mother's Bedroom": {"north": "Kitchen", "items": ["Mother's precious necklace"]},
    "Mother's Bathroom": {"west": "Mother's Bedroom", "items": ["Mother's favorite perfume"]}
}

if __name__ == "__main__":
    game()
