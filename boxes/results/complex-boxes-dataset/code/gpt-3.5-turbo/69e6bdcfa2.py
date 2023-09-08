# Initial state of boxes
boxes = {
    0: ['mirror', 'island', 'star'],
    1: [],
    2: ['mask'],
    3: ['blender', 'bell', 'violin'],
    4: ['earring', 'glasses', 'headphone', 'battery', 'beach'],
    5: [],
    6: ['sock']
}

# Replace the sock with the star in Box 6.
boxes[6].remove('sock')
boxes[6].append('star')

# Move the star from Box 6 to Box 3.
boxes[6].remove('star')
boxes[3].append('star')

# Move the star and the bell from Box 3 to Box 4.
boxes[3].remove('star')
boxes[3].remove('bell')
boxes[4].append('star')
boxes[4].append('bell')

# Swap the mirror in Box 0 with the mask in Box 2.
boxes[0].remove('mirror')
boxes[2].remove('mask')
boxes[0].append('mask')
boxes[2].append('mirror')

# Empty Box 3.
boxes[3] = []

# Remove the earring and the bell from Box 4.
boxes[4].remove('earring')
boxes[4].remove('bell')

# Remove the island from Box 0.
boxes[0].remove('island')

# Put the toy and the comet into Box 0.
boxes[0].append('toy')
boxes[0].append('comet')

# Move the mirror from Box 2 to Box 5.
boxes[2].remove('mirror')
boxes[5].append('mirror')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")