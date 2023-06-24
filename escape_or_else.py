# Clean-Up or ELSE Game

import random


# Game Instructions
def show_instructions():
    print("""
You are in your house.
Collect all items without mother noticing.
Move to any connected room by typing 'go' followed by the direction (north, south, east, or west).
Pick up items in the room by typing 'get' followed by the name of the item.
If mother is in the same room, you'll have to roll a die to hide or escape.
If you're caught, game over!
""")


# Player's Current Status
def get_status(current_room, inventory, mother_room):
    print("-----------------------------")
    print("You are in the", current_room)
    if mother_room == current_room:
        print("Mother is in the room with you!")
    else:
        connected_rooms = [room for room in rooms[current_room].values() if room != "items"]
        if mother_room in connected_rooms:
            print(f"You hear Mother's hums coming from {mother_room}.")
    print("Inventory:", ', '.join(inventory))
    if rooms[current_room]["items"]:
        print("You see:", ', '.join(rooms[current_room]["items"]))
    else:
        print("There's nothing to collect here.")
    for direction, room in rooms[current_room].items():
        if direction != "items":
            print(f"Go {direction.capitalize()} to enter {room}")
    print("-----------------------------")


# Dice Roll
def roll_dice(player_inventory):
    return random.randint(1, 20) + len(player_inventory)


# Hide or Escape
def attempt_escape(player_inventory):
    player_roll = roll_dice(player_inventory)
    mother_roll = random.randint(1, 20)
    action = input("Mother has entered the room! Will you hide or escape? ").lower()
    if player_roll > mother_roll:
        print(f"You successfully {action} from Mother!")
        return True
    else:
        print(f"You failed to {action}, Mother is suspicious but she's distracted.")
        print("You have one more chance...")
        player_roll = roll_dice(player_inventory)
        mother_roll = random.randint(1, 20)
        if player_roll > mother_roll:
            print(f"You successfully {action} on your second attempt!")
            return True
        else:
            print("You're caught. Game Over.")
            return False


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
    for direction in connected_rooms:
        print(f"- {direction.capitalize()} to enter {rooms[player_room][direction]}")
    while True:
        choice = input("Where do you want to escape to? ").lower()
        if choice in connected_rooms:
            return rooms[player_room][choice]
        else:
            print("Invalid choice. Try again.")


# Main Game Loop
def game():
    show_instructions()
    player_room = "Kitchen"
    player_inventory = []
    mother_room = "Mother's Bedroom"
    while True:
        try:
            if mother_room == player_room:
                if not attempt_escape(player_inventory):
                    break
                mother_room = move_mother(mother_room)
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
        except IndexError:
            print("Invalid command. Try again.")
            continue
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
