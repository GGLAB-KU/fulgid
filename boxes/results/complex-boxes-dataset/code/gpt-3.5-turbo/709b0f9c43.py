# Initial state of boxes
boxes = {
    0: ['pot', 'headphone', 'mask', 'coat'],
    1: ['keyboard', 'desert', 'watch', 'paint'],
    2: [],
    3: ['shoe', 'fridge', 'mixer', 'chair'],
    4: ['rocket', 'whistle', 'tree', 'drum'],
    5: ['table', 'glasses', 'tiger'],
    6: ['pan', 'vase', 'microwave', 'towel', 'tie']
}

# Move the glasses and the table and the tiger from Box 5 to Box 4.
items_to_move = ['glasses', 'table', 'tiger']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Put the rain into Box 0.
boxes[0].append('rain')

# Move the pot and the headphone from Box 0 to Box 5.
items_to_move = ['pot', 'headphone']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[5].append(item)

# Move the shoe from Box 3 to Box 4.
boxes[3].remove('shoe')
boxes[4].append('shoe')

# Remove the chair and the mixer from Box 3.
items_to_remove = ['chair', 'mixer']
for item in items_to_remove:
    boxes[3].remove(item)

# Remove the tie from Box 6.
boxes[6].remove('tie')

# Remove the fridge from Box 3.
boxes[3].remove('fridge')

# Remove the whistle from Box 4.
boxes[4].remove('whistle')

# Replace the microwave and the pan and the vase with the planet and the card and the bus in Box 6.
boxes[6].remove('microwave')
boxes[6].remove('pan')
boxes[6].remove('vase')
boxes[6].append('planet')
boxes[6].append('card')
boxes[6].append('bus')

# Swap the rain in Box 0 with the drum in Box 4.
boxes[0].remove('rain')
boxes[4].remove('drum')
boxes[0].append('drum')
boxes[4].append('rain')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")