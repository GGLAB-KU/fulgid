# Initial state of boxes
boxes = {
    0: ['perfume', 'jacket', 'hat', 'polish', 'plate'],
    1: [],
    2: ['desert', 'plane', 'headphone'],
    3: ['flute', 'thread', 'pillow', 'bag', 'card'],
    4: ['crown', 'coin', 'chair', 'razor', 'laptop'],
    5: [],
    6: ['pot', 'brush', 'helmet', 'shirt']
}

# Put the magnet into Box 4.
boxes[4].append('magnet')

# Put the tie into Box 2.
boxes[2].append('tie')

# Swap the laptop in Box 4 with the polish in Box 0.
boxes[0].remove('polish')
boxes[4].remove('laptop')
boxes[0].append('laptop')
boxes[4].append('polish')

# Put the key and the moon and the piano into Box 0.
items_to_put = ['key', 'moon', 'piano']
for item in items_to_put:
    boxes[0].append(item)

# Remove the helmet and the shirt from Box 6.
boxes[6].remove('helmet')
boxes[6].remove('shirt')

# Swap the pot in Box 6 with the bag in Box 3.
boxes[3].remove('bag')
boxes[6].remove('pot')
boxes[3].append('pot')
boxes[6].append('bag')

# Move the desert and the plane and the tie from Box 2 to Box 1.
items_to_move = ['desert', 'plane', 'tie']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Replace the chair and the magnet with the cup and the telescope in Box 4.
boxes[4].remove('chair')
boxes[4].remove('magnet')
boxes[4].append('cup')
boxes[4].append('telescope')

# Move the polish from Box 4 to Box 1.
boxes[4].remove('polish')
boxes[1].append('polish')

# Move the flute from Box 3 to Box 2.
boxes[3].remove('flute')
boxes[2].append('flute')

# Replace the telescope with the mixer in Box 4.
boxes[4].remove('telescope')
boxes[4].append('mixer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")