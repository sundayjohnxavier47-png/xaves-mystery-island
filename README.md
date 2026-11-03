# Mystery Island: The Lost Lighthouse

A text adventure in Python. You wake up on Mystery Island after a storm.
The lighthouse is dark and the bridge is locked. Restore the beacon to be rescued.

## Map
Beach → Jungle → Cave → Old Bridge → Lighthouse
(Movement uses north / south / east / west.)

## Player state
- name, location, energy (starts at 5), inventory (starts empty), game_over, won

## Items
- Lantern: found in the Jungle
- Rope: found in the Cave
- Each item can be collected only once.

## Rules
- Every legal move costs 1 energy.
- Invalid input and moves with no path cost nothing.
- Lighting the beacon at the Lighthouse requires the lantern.
- Menu text includes small hints, for example: "The shadows point south."

## Win / Lose
- Win: beacon lit while energy remains.
- Lose: energy reaches 0 before the beacon is lit.

## Known limits
- TO FILL IN as the game grows.