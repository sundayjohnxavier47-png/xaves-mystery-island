# Mystery Island: The Lost Lighthouse

A text adventure written in Python. You wake up on Mystery Island after a storm.
The lighthouse is dark, the bridge is locked, and a rescue boat will come only
if you restore the beacon.

## Setup
1. Install Python 3.
2. Clone this repository and open the folder.
3. (Optional) Create a virtual environment: `python3 -m venv .venv`, then `source .venv/bin/activate`.
4. Run the game: `python main.py`
5. Run the tests: `python -m unittest discover -s tests -v`

No extra packages are needed. The game uses only the Python standard library.

## How to play
Type a command and press Enter. Commands are not case sensitive, and extra spaces are ignored.

| Command | What it does |
|---|---|
| north / south / east / west | Move in that direction |
| take | Pick up the item in the current place |
| inventory | Show what you are carrying |
| search | Search the swamp (swamp only) |
| light | Light the beacon (lighthouse only) |
| quit | Leave the game |

## Map
Beach → Jungle → Cave → Old Bridge → Lighthouse

- Going north moves you toward the lighthouse. Going south moves you back.
- The Swamp is a dead end east of the Jungle. Go west to return.
- Menu text includes small hints, for example: "The shadows point south."

## Player state
- name, location, energy, inventory, game_over, won
- A new game starts at the Beach with 5 energy and an empty inventory.

## Items
- Lantern: found in the Jungle.
- Rope: found in the Cave.
- Each item can be collected only once. Picking up an item costs no energy.

## Rules
- Every legal move costs 1 energy.
- A direction with no path is rejected and costs nothing.
- Moving into the Swamp is a legal move and costs 1 energy.
- Invalid input is rejected, costs nothing and changes nothing.
- Energy can never go below 0.
- Rules are deterministic: the same state and the same action always give the same result.

## Decisions and consequences
1. Cave without the lantern: you get lost and the game ends in a loss.
   With the lantern, you see a hint that a rope is nearby.
2. Old Bridge without the rope: you cannot cross to the Lighthouse.
3. Swamp: searching costs 1 energy and restores your energy to full (5).
   You can do it only once. Is the detour worth it?

## How to win or lose
- Win: reach the Lighthouse with the lantern and use `light` while you still have energy.
- Lose: energy reaches 0 before the beacon is lit, or you get lost in the Cave.
- After the game ends, you can choose to play again. A new game resets energy,
  location and inventory.

## Known limits
- Text commands only, no graphics.
- One player, no save files.
- To be updated as the game grows.