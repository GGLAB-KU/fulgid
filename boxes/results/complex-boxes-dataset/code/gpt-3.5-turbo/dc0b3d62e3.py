# Initial state of boxes
boxes = {
    0: ['rock', 'flute', 'scissors', 'storm', 'telescope'],
    1: [],
    2: ['book', 'elephant', 'tie'],
    3: ['table', 'cloud', 'cup', 'brush', 'note'],
    4: [],
    5: ['game'],
    6: ['bracelet', 'laptop', 'oven', 'speaker']
}

# Swap the note in Box 3 with the oven in Box 6.
boxes[3].remove('note')
boxes[6].remove('oven')
boxes[3].append('oven')
boxes[6].append('note')

# Replace the note and the laptop and the bracelet with the pillow and the gloves and the watch in Box 6.
boxes[3].remove('note')
boxes[6].remove('laptop')
boxes[6].remove('bracelet')
boxes[6].append('pillow')
boxes[6].append('gloves')
boxes[6].append('watch')

# Swap the game in Box 5 with the brush in Box 3.
boxes[5].remove('game')
boxes[3].remove('brush')
boxes[5].append('brush')
boxes[3].append('game')

# Replace the tie and the elephant with the ship and the phone in Box 2.
boxes[2].remove('tie')
boxes[2].remove('elephant')
boxes[2].append('ship')
boxes[2].append('phone')

# Put the lipstick and the drum into Box 2.
boxes[2].append('lipstick')
boxes[2].append('drum')

# Swap the drum in Box 2 with the cloud in Box 3.
boxes[2].remove('drum')
boxes[3].remove('cloud')
boxes[2].append('cloud')
boxes[3].append('drum')

# Move the gloves and the watch from Box 6 to Box 5.
boxes[6].remove('gloves')
boxes[6].remove('watch')
boxes[5].append('gloves')
boxes[5].append('watch')

# Replace the phone with the pot in Box 2.
boxes[2].remove('phone')
boxes[2].append('pot')

# Put the telescope into Box 6.
boxes[6].append('telescope')

# Put the horn and the mask and the tie into Box 0.
boxes[0].append('horn')
boxes[0].append('mask')
boxes[0].append('tie')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")