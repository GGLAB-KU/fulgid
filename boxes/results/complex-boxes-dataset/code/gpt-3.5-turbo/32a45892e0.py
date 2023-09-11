# Initial state of boxes
boxes = {
    0: ['zipper', 'ocean', 'rain', 'swimsuit'],
    1: ['snow', 'desert'],
    2: ['cup', 'cat'],
    3: [],
    4: ['usb', 'telescope']
}

# Swap the usb in Box 4 with the snow in Box 1.
boxes[1].remove('snow')
boxes[4].remove('usb')
boxes[1].append('usb')
boxes[4].append('snow')

# Remove the swimsuit and the ocean from Box 0.
boxes[0].remove('swimsuit')
boxes[0].remove('ocean')

# Swap the telescope in Box 4 with the cup in Box 2.
boxes[2].remove('cup')
boxes[4].remove('telescope')
boxes[2].append('telescope')
boxes[4].append('cup')

# Replace the desert and the usb with the bag and the button in Box 1.
boxes[1].remove('desert')
boxes[4].remove('usb')
boxes[1].append('bag')
boxes[4].append('button')

# Remove the bag and the button from Box 1.
boxes[1].remove('bag')
boxes[1].remove('button')

# Replace the rain and the zipper with the dice and the jungle in Box 0.
boxes[0].remove('rain')
boxes[0].remove('zipper')
boxes[0].append('dice')
boxes[0].append('jungle')

# Put the tree and the pillow and the starfish into Box 2.
items_to_move = ['tree', 'pillow', 'starfish']
for item in items_to_move:
    boxes[2].append(item)

# Put the mask and the crown into Box 4.
items_to_move = ['mask', 'crown']
for item in items_to_move:
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")