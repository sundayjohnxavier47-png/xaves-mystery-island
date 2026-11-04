print("*MYSTERY ISLAND*")
print("Welcome to Mystery Island. \nYou wake up on Mystery Island after a storm. \nThe lighthouse is dark, the bridge is locked, and a rescue boat will arrive only if you restore the beacon. \nBegin your adventure in which the you explore locations, collects objects, solves simple puzzles and escape. \nTry not to run out of energy.")
name = input("Choose a character name: ")
name = name.strip()
location = "Beach"
energy = 5
running = True
while running:
    print(f"Hello {name}. \nYou are at {location}")
    answer = input("Choose direction to walk: North, South, East, West or Quit\n the shadows are pointing south\n")
    answer = answer.strip().lower()
    if answer == "quit":
        print(f"Goodbye {name}")
        break