# Initial state of boxes
boxes = {
    0: ['toy', 'game', 'jacket', 'cup', 'tree'],
    1: ['swimsuit', 'shark'],
    2: ['glove', 'shorts'],
    3: ['wallet', 'battery', 'blender'],
    4: ['comet'],
    5: ['bracelet', 'fork'],
    6: ['octopus', 'towel', 'pillow'],
    7: ['puzzle', 'console', 'car', 'thread', 'flower'],
    8: ['microscope', 'watch', 'book', 'moon'],
    9: ['storm', 'bird', 'shoe'],
    10: ['island', 'magnet', 'rocket']
}

# Replace the comet with the doll in Box 4.
boxes[4].remove('comet')
boxes[4].append('doll')

# Swap the wallet in Box 3 with the bird in Box 9.
boxes[3].remove('wallet')
boxes[9].remove('bird')
boxes[3].append('bird')
boxes[9].append('wallet')

# Replace the watch with the console in Box 8.
boxes[8].remove('watch')
boxes[8].append('console')

# Swap the blender in Box 3 with the microscope in Box 8.
boxes[3].remove('blender')
boxes[8].remove('microscope')
boxes[3].append('microscope')
boxes[8].append('blender')

# Replace the doll with the snow in Box 4.
boxes[4].remove('doll')
boxes[4].append('snow')

# Put the coin and the truck into Box 7.
boxes[7].append('coin')
boxes[7].append('truck')

# Remove the shorts from Box 2.
boxes[2].remove('shorts')

# Move the shoe and the wallet from Box 9 to Box 10.
boxes[9].remove('shoe')
boxes[9].remove('wallet')
boxes[10].append('shoe')
boxes[10].append('wallet')

# Swap the glove in Box 2 with the battery in Box 3.
boxes[2].remove('glove')
boxes[3].remove('battery')
boxes[2].append('battery')
boxes[3].append('glove')

# Put the shorts into Box 6.
boxes[6].append('shorts')

# Replace the bird with the mask in Box 3.
boxes[3].remove('bird')
boxes[3].append('mask')

# Put the cow and the soap and the seaweed into Box 8.
boxes[8].append('cow')
boxes[8].append('soap')
boxes[8].append('seaweed')

# Put the horn and the controller into Box 8.
boxes[8].append('horn')
boxes[8].append('controller')

# Remove the truck and the car from Box 7.
boxes[7].remove('truck')
boxes[7].remove('car')

# Put the polish into Box 3.
boxes[3].append('polish')

# Put the car and the gloves and the truck into Box 4.
boxes[4].append('car')
boxes[4].append('gloves')
boxes[4].append('truck')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")