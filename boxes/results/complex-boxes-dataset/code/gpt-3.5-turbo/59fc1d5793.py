# Initial state of boxes
boxes = {
    0: ['elephant', 'bear', 'magnet', 'star', 'battery'],
    1: ['snow', 'wallet'],
    2: ['headphone', 'ring', 'perfume', 'wig', 'ship'],
    3: ['game'],
    4: ['submarine', 'pen', 'charger'],
    5: ['basket', 'octopus', 'lamp', 'horn'],
    6: ['speaker', 'cat'],
    7: []
}

# Remove the speaker from Box 6.
boxes[6].remove('speaker')

# Swap the ship in Box 2 with the magnet in Box 0.
boxes[0].remove('magnet')
boxes[2].remove('ship')
boxes[0].append('ship')
boxes[2].append('magnet')

# Replace the horn and the basket and the octopus with the comet and the apple and the toy in Box 5.
boxes[5].remove('horn')
boxes[5].remove('basket')
boxes[5].remove('octopus')
boxes[5].append('comet')
boxes[5].append('apple')
boxes[5].append('toy')

# Swap the game in Box 3 with the wallet in Box 1.
boxes[1].remove('wallet')
boxes[3].remove('game')
boxes[1].append('game')
boxes[3].append('wallet')

# Empty Box 1.
boxes[1] = []

# Move the wallet from Box 3 to Box 0.
boxes[3].remove('wallet')
boxes[0].append('wallet')

# Replace the pen and the submarine and the charger with the lamp and the truck and the fork in Box 4.
boxes[4].remove('pen')
boxes[4].remove('submarine')
boxes[4].remove('charger')
boxes[4].append('lamp')
boxes[4].append('truck')
boxes[4].append('fork')

# Remove the apple from Box 5.
boxes[5].remove('apple')

# Swap the cat in Box 6 with the toy in Box 5.
boxes[5].remove('toy')
boxes[6].remove('cat')
boxes[5].append('cat')
boxes[6].append('toy')

# Move the cat and the comet from Box 5 to Box 1.
boxes[5].remove('cat')
boxes[5].remove('comet')
boxes[1].append('cat')
boxes[1].append('comet')

# Replace the lamp with the train in Box 5.
boxes[5].remove('lamp')
boxes[5].append('train')

# Move the wallet from Box 0 to Box 1.
boxes[0].remove('wallet')
boxes[1].append('wallet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")