# Initial state of boxes
boxes = {
    0: ['wallet'],
    1: ['bowl'],
    2: ['button', 'forest', 'motorcycle'],
    3: ['sock', 'cloud', 'comet', 'bicycle'],
    4: [],
    5: ['battery', 'ship', 'towel', 'speaker', 'telescope'],
    6: ['bus', 'coral', 'thread', 'blender', 'console'],
    7: ['bird'],
    8: []
}

# Put the lock and the chair and the horn into Box 3.
boxes[3].extend(['lock', 'chair', 'horn'])

# Put the mixer and the scissors and the shampoo into Box 8.
boxes[8].extend(['mixer', 'scissors', 'shampoo'])

# Swap the chair in Box 3 with the wallet in Box 0.
boxes[0].remove('wallet')
boxes[3].remove('chair')
boxes[0].append('chair')
boxes[3].append('wallet')

# Put the cloud and the button into Box 4.
boxes[4].extend(['cloud', 'button'])

# Remove the bowl from Box 1.
boxes[1].remove('bowl')

# Put the mirror and the cup and the fork into Box 1.
boxes[1].extend(['mirror', 'cup', 'fork'])

# Remove the scissors and the mixer from Box 8.
boxes[8].remove('scissors')
boxes[8].remove('mixer')

# Put the sandals into Box 8.
boxes[8].append('sandals')

# Put the blanket into Box 0.
boxes[0].append('blanket')

# Remove the shampoo from Box 8.
boxes[8].remove('shampoo')

# Remove the sock and the horn and the lock from Box 3.
boxes[3].remove('sock')
boxes[3].remove('horn')
boxes[3].remove('lock')

# Replace the ship and the battery with the watch and the cloud in Box 5.
boxes[5].remove('ship')
boxes[5].remove('battery')
boxes[5].append('watch')
boxes[5].append('cloud')

# Empty Box 0.
boxes[0] = []

# Move the button from Box 4 to Box 0.
boxes[4].remove('button')
boxes[0].append('button')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")