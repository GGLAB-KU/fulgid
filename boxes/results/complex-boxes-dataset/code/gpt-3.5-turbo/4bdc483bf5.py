# Initial state of boxes
boxes = {
    0: ['earring', 'pan', 'tiger', 'snow'],
    1: ['laptop', 'paint', 'needle'],
    2: ['shoes', 'lipstick'],
    3: ['shorts', 'lamp'],
    4: ['shoe', 'key', 'branch', 'puzzle']
}

# Swap the paint in Box 1 with the earring in Box 0.
boxes[0].remove('earring')
boxes[1].remove('paint')
boxes[0].append('paint')
boxes[1].append('earring')

# Replace the pan and the tiger and the snow with the doll and the planet and the ocean in Box 0.
boxes[0].remove('pan')
boxes[0].remove('tiger')
boxes[0].remove('snow')
boxes[0].append('doll')
boxes[0].append('planet')
boxes[0].append('ocean')

# Remove the needle and the earring and the laptop from Box 1.
boxes[1].remove('needle')
boxes[1].remove('earring')
boxes[1].remove('laptop')

# Replace the lamp with the spoon in Box 3.
boxes[3].remove('lamp')
boxes[3].append('spoon')

# Replace the puzzle and the key and the branch with the umbrella and the ship and the fish in Box 4.
boxes[4].remove('puzzle')
boxes[4].remove('key')
boxes[4].remove('branch')
boxes[4].append('umbrella')
boxes[4].append('ship')
boxes[4].append('fish')

# Remove the paint from Box 0.
boxes[0].remove('paint')

# Swap the spoon in Box 3 with the planet in Box 0.
boxes[0].remove('planet')
boxes[3].remove('spoon')
boxes[0].append('spoon')
boxes[3].append('planet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")