# Initial state of boxes
boxes = {
    0: ['branch', 'laptop', 'soap'],
    1: ['card', 'perfume'],
    2: [],
    3: ['island', 'razor'],
    4: [],
    5: ['spoon', 'bell', 'grinder'],
    6: ['guitar', 'grass', 'freezer', 'earring'],
    7: ['lion', 'shark', 'belt'],
    8: ['rocket', 'starfish', 'violin', 'motorcycle']
}

# Empty Box 5.
boxes[5] = []

# Swap the motorcycle in Box 8 with the razor in Box 3.
boxes[8].remove('motorcycle')
boxes[3].remove('razor')
boxes[8].append('razor')
boxes[3].append('motorcycle')

# Remove the starfish and the razor from Box 8.
boxes[8].remove('starfish')
boxes[8].remove('razor')

# Remove the rocket and the violin from Box 8.
boxes[8].remove('rocket')
boxes[8].remove('violin')

# Remove the shark and the belt and the lion from Box 7.
boxes[7].remove('shark')
boxes[7].remove('belt')
boxes[7].remove('lion')

# Remove the grass and the earring and the freezer from Box 6.
boxes[6].remove('grass')
boxes[6].remove('earring')
boxes[6].remove('freezer')

# Remove the soap and the branch from Box 0.
boxes[0].remove('soap')
boxes[0].remove('branch')

# Put the fork into Box 2.
boxes[2].append('fork')

# Swap the guitar in Box 6 with the motorcycle in Box 3.
boxes[6].remove('guitar')
boxes[3].remove('motorcycle')
boxes[6].append('motorcycle')
boxes[3].append('guitar')

# Replace the island with the fork in Box 3.
boxes[3].remove('island')
boxes[3].append('fork')

# Move the fork from Box 3 to Box 1.
boxes[3].remove('fork')
boxes[1].append('fork')

# Swap the fork in Box 2 with the guitar in Box 3.
boxes[2].remove('fork')
boxes[3].remove('guitar')
boxes[2].append('guitar')
boxes[3].append('fork')

# Empty Box 3.
boxes[3] = []

# Put the laptop into Box 5.
boxes[5].append('laptop')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")