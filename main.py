print("*MYSTERY ISLAND*")
print("Welcome to Mystery Island. \nYou wake up on Mystery Island after a storm. \nThe lighthouse is dark, the bridge is locked, and a rescue boat will arrive only if you restore the beacon. \nBegin your adventure in which the you explore locations, collects objects, solves simple puzzles and escape. \nTry not to run out of energy.")
name = input("Choose a character name: ")
name = name.strip()
location = "Beach"
energy = 5
running = True
print(f"Hello {name}. \nYou are at {location}")

while running:
    answer = input("Choose direction to walk: North, South, East, West or Quit\n the shadows are pointing south\n")
    answer = answer.strip().lower()
    if answer == "quit":
        print(f"Goodbye {name}")
         print(f"Energy left: {energy}")
    elif answer == "north":
        print("You walk north and find a dense jungle. You hear strange noises.")
        location = "Jungle"
        energy -= 1
        print(energy)
         print(f"Energy left: {energy}")
    elif answer == "south":
        print("You walk south and find a dark cave. You see glowing eyes staring at you.")
        location = "Cave"
        energy -= 1
        print(energy)
        print(f"Energy left: {energy}")
    elif answer == "east":
        print("You walk east and find an old bridge. The bridge is locked but you cannot cross it.")
        location = "Old Bridge"
        energy -= 1
        print(energy)
        print(f"Energy left: {energy}")
    elif answer == "west":
        print("You walk west and find a Lighthouse. The lighthouse is locked but you can see the beacon. You need to restore the beacon to signal for help.")
        location = "Lighthouse"
        energy += 1
        print(energy)
        print(f"Energy left: {energy}")
    else:
        print("Invalid direction. Please choose North, South, East, West or Quit.")