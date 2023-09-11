# Initial state of boxes
boxes = {
    0: ['octopus', 'oven'],
    1: ['game', 'polish'],
    2: ['forest', 'seaweed'],
    3: ['branch']
}

# Remove the polish from Box 1.
boxes[1].remove('polish')

# Swap the octopus in Box 0 with the forest in Box 2.
boxes[0].remove('octopus')
boxes[2].remove('forest')
boxes[0].append('forest')
boxes[2].append('octopus')

# Replace the game with the motorcycle in Box 1.
boxes[1].remove('game')
boxes[1].append('motorcycle')

# Move the branch from Box 3 to Box 1.
boxes[3].remove('branch')
boxes[1].append('branch')

# Put the microwave and the game into Box 0.
boxes[0].append('microwave')
boxes[0].append('game')

# Empty Box 2.
boxes[2] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")