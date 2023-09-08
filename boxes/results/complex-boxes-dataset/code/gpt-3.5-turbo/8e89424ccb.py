# Initial state of boxes
boxes = {
    0: ['wig', 'mixer', 'train', 'shelf', 'drum'],
    1: ['toaster', 'river'],
    2: ['candle', 'necklace'],
    3: [],
    4: ['table', 'planet', 'crown', 'horse', 'clock']
}

# Move the clock and the planet and the table from Box 4 to Box 1.
items_to_move = ['clock', 'planet', 'table']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[1].append(item)

# Swap the candle in Box 2 with the horse in Box 4.
boxes[2].remove('candle')
boxes[4].remove('horse')
boxes[2].append('horse')
boxes[4].append('candle')

# Replace the candle with the freezer in Box 4.
boxes[4].remove('candle')
boxes[4].append('freezer')

# Put the sandals into Box 1.
boxes[1].append('sandals')

# Remove the mixer and the drum and the wig from Box 0.
items_to_remove = ['mixer', 'drum', 'wig']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the necklace and the horse from Box 2 to Box 4.
items_to_move = ['necklace', 'horse']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[4].append(item)

# Put the bag and the thunder into Box 1.
items_to_put = ['bag', 'thunder']
for item in items_to_put:
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")