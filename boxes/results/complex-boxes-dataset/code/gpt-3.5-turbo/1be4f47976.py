# Initial state of boxes
boxes = {
    0: ['razor', 'fork', 'moon'],
    1: ['sock'],
    2: ['boot', 'bear', 'zipper', 'headphone'],
    3: ['branch'],
    4: ['octopus', 'elephant', 'dog'],
    5: []
}

# Put the crown and the key and the table into Box 3.
boxes[3].extend(['crown', 'key', 'table'])

# Put the keyboard and the bicycle and the flute into Box 1.
boxes[1].extend(['keyboard', 'bicycle', 'flute'])

# Replace the razor and the fork with the island and the thunder in Box 0.
boxes[0].remove('razor')
boxes[0].remove('fork')
boxes[0].extend(['island', 'thunder'])

# Put the note and the thunder and the mountain into Box 3.
boxes[3].extend(['note', 'thunder', 'mountain'])

# Empty Box 3.
boxes[3] = []

# Remove the dog and the octopus and the elephant from Box 4.
boxes[4].remove('dog')
boxes[4].remove('octopus')
boxes[4].remove('elephant')

# Put the car and the coat into Box 4.
boxes[4].extend(['car', 'coat'])

# Remove the sock and the keyboard from Box 1.
boxes[1].remove('sock')
boxes[1].remove('keyboard')

# Replace the flute and the bicycle with the razor and the magnet in Box 1.
boxes[1].remove('flute')
boxes[1].remove('bicycle')
boxes[1].extend(['razor', 'magnet'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")