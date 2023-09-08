# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['whistle', 'doll'],
    3: ['cloud', 'grinder', 'flute'],
    4: ['motorcycle'],
    5: ['shorts', 'sun'],
    6: ['necklace', 'river', 'watch'],
    7: ['vase', 'bird', 'moon', 'bicycle', 'gloves']
}

# Put the game and the moon into Box 7.
boxes[7].append('game')
boxes[7].append('moon')

# Put the apple into Box 1.
boxes[1].append('apple')

# Empty Box 4.
boxes[4] = []

# Put the guitar into Box 2.
boxes[2].append('guitar')

# Swap the watch in Box 6 with the guitar in Box 2.
boxes[6].remove('watch')
boxes[2].remove('guitar')
boxes[6].append('guitar')
boxes[2].append('watch')

# Swap the gloves in Box 7 with the sun in Box 5.
boxes[7].remove('gloves')
boxes[5].remove('sun')
boxes[7].append('sun')
boxes[5].append('gloves')

# Replace the river and the guitar and the necklace with the vase and the island and the plane in Box 6.
boxes[6].remove('river')
boxes[6].remove('guitar')
boxes[6].remove('necklace')
boxes[6].append('vase')
boxes[6].append('island')
boxes[6].append('plane')

# Swap the apple in Box 1 with the shorts in Box 5.
boxes[1].remove('apple')
boxes[5].remove('shorts')
boxes[1].append('shorts')
boxes[5].append('apple')

# Put the sculpture and the pan into Box 6.
boxes[6].append('sculpture')
boxes[6].append('pan')

# Replace the pan and the plane with the octopus and the watch in Box 6.
boxes[6].remove('pan')
boxes[6].remove('plane')
boxes[6].append('octopus')
boxes[6].append('watch')

# Remove the doll from Box 2.
boxes[2].remove('doll')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")