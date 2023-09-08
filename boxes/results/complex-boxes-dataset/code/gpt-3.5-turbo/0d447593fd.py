# Initial state of boxes
boxes = {
    0: ['plate'],
    1: ['bus', 'game', 'charger', 'submarine', 'hat'],
    2: ['river', 'horn', 'pillow'],
    3: ['mixer'],
    4: ['boat']
}

# Remove the boat from Box 4.
boxes[4].remove('boat')

# Put the lightning and the controller into Box 1.
boxes[1].append('lightning')
boxes[1].append('controller')

# Put the fish and the thunder into Box 3.
boxes[3].append('fish')
boxes[3].append('thunder')

# Move the pillow and the river from Box 2 to Box 1.
items_to_move = ['pillow', 'river']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Put the chair and the starfish and the fork into Box 1.
items_to_put = ['chair', 'starfish', 'fork']
for item in items_to_put:
    boxes[1].append(item)

# Replace the mixer and the fish with the doll and the glasses in Box 3.
boxes[3].remove('mixer')
boxes[3].remove('fish')
boxes[3].append('doll')
boxes[3].append('glasses')

# Put the keyboard into Box 3.
boxes[3].append('keyboard')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")