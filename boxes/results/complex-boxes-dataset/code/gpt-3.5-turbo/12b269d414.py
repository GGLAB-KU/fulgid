# Initial state of boxes
boxes = {
    0: [],
    1: ['necklace', 'seaweed', 'lock', 'rocket'],
    2: ['doll', 'telescope', 'tree', 'car', 'fridge'],
    3: ['thunder', 'skirt', 'butterfly', 'toy'],
    4: ['razor'],
    5: ['wallet', 'coral', 'belt', 'ship', 'freezer'],
    6: ['pot', 'motorcycle', 'shorts'],
    7: ['bowl'],
    8: ['plane'],
    9: ['glove', 'note', 'earring', 'rain', 'star']
}

# Replace the doll and the tree and the fridge with the star and the hat and the octopus in Box 2.
boxes[2].remove('doll')
boxes[2].remove('tree')
boxes[2].remove('fridge')
boxes[2].append('star')
boxes[2].append('hat')
boxes[2].append('octopus')

# Move the pot and the motorcycle from Box 6 to Box 2.
boxes[6].remove('pot')
boxes[6].remove('motorcycle')
boxes[2].append('pot')
boxes[2].append('motorcycle')

# Swap the shorts in Box 6 with the wallet in Box 5.
boxes[6].remove('shorts')
boxes[5].remove('wallet')
boxes[6].append('wallet')
boxes[5].append('shorts')

# Remove the plane from Box 8.
boxes[8].remove('plane')

# Remove the seaweed and the lock from Box 1.
boxes[1].remove('seaweed')
boxes[1].remove('lock')

# Remove the thunder from Box 3.
boxes[3].remove('thunder')

# Swap the rain in Box 9 with the rocket in Box 1.
boxes[9].remove('rain')
boxes[1].remove('rocket')
boxes[9].append('rocket')
boxes[1].append('rain')

# Empty Box 5.
boxes[5] = []

# Replace the butterfly and the skirt with the headphone and the perfume in Box 3.
boxes[3].remove('butterfly')
boxes[3].remove('skirt')
boxes[3].append('headphone')
boxes[3].append('perfume')

# Replace the bowl with the tree in Box 7.
boxes[7].remove('bowl')
boxes[7].append('tree')

# Move the pot and the car from Box 2 to Box 1.
boxes[2].remove('pot')
boxes[2].remove('car')
boxes[1].append('pot')
boxes[1].append('car')

# Remove the rocket and the glove from Box 9.
boxes[9].remove('rocket')
boxes[9].remove('glove')

# Replace the wallet with the bus in Box 6.
boxes[6].remove('wallet')
boxes[6].append('bus')

# Swap the car in Box 1 with the motorcycle in Box 2.
boxes[1].remove('car')
boxes[2].remove('motorcycle')
boxes[1].append('motorcycle')
boxes[2].append('car')

# Move the bus from Box 6 to Box 9.
boxes[6].remove('bus')
boxes[9].append('bus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")