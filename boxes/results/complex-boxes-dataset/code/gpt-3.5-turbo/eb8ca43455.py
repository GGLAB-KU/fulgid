# Initial state of boxes
boxes = {
    0: [],
    1: ['horse', 'puzzle', 'earring', 'desert', 'comet'],
    2: [],
    3: ['note', 'controller', 'mountain', 'lipstick'],
    4: ['shampoo'],
    5: ['scarf'],
    6: ['lock', 'coral', 'planet', 'key'],
    7: ['drum', 'shoes', 'bag', 'perfume', 'moon'],
    8: []
}

# Put the car into Box 3.
boxes[3].append('car')

# Remove the shampoo from Box 4.
boxes[4].remove('shampoo')

# Put the microscope and the river into Box 7.
boxes[7].append('microscope')
boxes[7].append('river')

# Remove the scarf from Box 5.
boxes[5].remove('scarf')

# Put the lightning and the storm into Box 1.
boxes[1].append('lightning')
boxes[1].append('storm')

# Put the wallet and the elephant and the glasses into Box 3.
boxes[3].append('wallet')
boxes[3].append('elephant')
boxes[3].append('glasses')

# Move the desert and the earring from Box 1 to Box 4.
boxes[1].remove('desert')
boxes[1].remove('earring')
boxes[4].append('desert')
boxes[4].append('earring')

# Swap the perfume in Box 7 with the coral in Box 6.
boxes[7].remove('perfume')
boxes[6].remove('coral')
boxes[7].append('coral')
boxes[6].append('perfume')

# Replace the perfume and the planet with the pillow and the island in Box 6.
boxes[6].remove('perfume')
boxes[6].remove('planet')
boxes[6].append('pillow')
boxes[6].append('island')

# Move the island and the key from Box 6 to Box 4.
boxes[6].remove('island')
boxes[6].remove('key')
boxes[4].append('island')
boxes[4].append('key')

# Put the key and the submarine and the desert into Box 5.
boxes[5].append('key')
boxes[5].append('submarine')
boxes[5].append('desert')

# Put the jacket and the plane and the storm into Box 4.
boxes[4].append('jacket')
boxes[4].append('plane')
boxes[4].append('storm')

# Move the earring from Box 4 to Box 5.
boxes[4].remove('earring')
boxes[5].append('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")