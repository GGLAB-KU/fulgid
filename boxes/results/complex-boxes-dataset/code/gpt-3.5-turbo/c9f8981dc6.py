# Initial state of boxes
boxes = {
    0: ['moon', 'hat', 'scissors'],
    1: ['keyboard'],
    2: ['microwave'],
    3: ['car', 'octopus', 'thunder', 'clock'],
    4: ['makeup'],
    5: [],
    6: []
}

# Move the makeup from Box 4 to Box 3.
boxes[4].remove('makeup')
boxes[3].append('makeup')

# Replace the microwave with the plane in Box 2.
boxes[2].remove('microwave')
boxes[2].append('plane')

# Empty Box 0.
boxes[0] = []

# Put the zipper and the starfish into Box 5.
boxes[5].append('zipper')
boxes[5].append('starfish')

# Put the lightning and the wig into Box 6.
boxes[6].append('lightning')
boxes[6].append('wig')

# Put the cat into Box 5.
boxes[5].append('cat')

# Empty Box 3.
boxes[3] = []

# Move the cat from Box 5 to Box 0.
boxes[5].remove('cat')
boxes[0].append('cat')

# Put the apple into Box 2.
boxes[2].append('apple')

# Remove the plane from Box 2.
boxes[2].remove('plane')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")