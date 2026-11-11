world = {
    "Beach": {"north": "Jungle"},
    "Jungle": {"south": "Beach", "north": "Cave"},
    "Cave": {"south": "Jungle", "north": "Old Bridge"},
    "Old Bridge": {"north": "Lighthouse", "south": "Cave"},
    "Lighthouse": {"south": "Old Bridge"}
}
items = {
    "Jungle": ["lantern"],
    "Cave": ["rope"],
}
inventory = []
print("*MYSTERY ISLAND*")
print("Welcome to Mystery Island. \nYou wake up on Mystery Island after a storm. \nThe lighthouse is dark, the bridge is locked, and a rescue boat will arrive only if you restore the beacon. \nBegin your adventure in which the you explore locations, collects objects, solves simple puzzles and escape. \nTry not to run out of energy.")
name = input("Choose a character name: ")
name = name.strip()
location = "Beach"
energy = 5
running = True
print(f"Hello {name}. \nYou are at {location}")

while running:
    print(f"Location: {location} | Energy: {energy}")
    answer = input("Choose direction to walk: North, South, East, West or Quit\n" )
    answer = answer.strip().lower()
    if answer == "quit":
        print(f"Goodbye {name}")
        running = False
    elif answer == "take":
        if answer in items.get(location, []):
            inventory.append(answer)
            items[location].remove(answer)
            print(f"You have taken the {answer}.")
        else:
            print(f"There is no {answer} here to take.")
    elif answer == "inventory":
        if inventory:
            print(f"You have the {item} in your inventory:")
        else:
            print("Your inventory is empty.")
    elif answer in world[location]:
        location = world[location][answer]
        energy -= 1
        print(f"You walk {answer} to {location}.")
        print(f"Energy remaining: {energy}")
    elif answer == "light":
        if location == "Lighthouse" and "lantern" in inventory:
            print("You light the lantern and restore the beacon. A rescue boat arrives! \nYou win!!!")
            running = False
        elif location == "Lighthouse" and "lantern" not in inventory:
            print("You need a lantern to light the beacon.")
        else:
            print("There is nothing to light here.")
    elif answer in ["north", "south", "east", "west"]:
        print(f"You can't go {answer} from {location}.")
    else:
        print("Invalid direction. Please choose North, South, East, West or Quit.")
    
