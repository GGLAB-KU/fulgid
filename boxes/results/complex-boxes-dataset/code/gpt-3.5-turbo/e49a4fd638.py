# Initial state of boxes
boxes = {
    0: ['skirt'],
    1: ['grinder', 'apple', 'watch'],
    2: [],
    3: ['mask', 'glasses'],
    4: ['ring', 'sandals'],
    5: ['coat', 'doll', 'basket'],
    6: ['grass', 'umbrella'],
    7: ['shampoo', 'fork'],
    8: ['bag', 'keyboard', 'bird', 'star']
}

# Put the tree into Box 3.
boxes[3].append('tree')

# Replace the grinder with the needle in Box 1.
boxes[1].remove('grinder')
boxes[1].append('needle')

# Swap the star in Box 8 with the sandals in Box 4.
boxes[8].remove('star')
boxes[4].remove('sandals')
boxes[8].append('sandals')
boxes[4].append('star')

# Remove the fork and the shampoo from Box 7.
boxes[7].remove('fork')
boxes[7].remove('shampoo')

# Swap the grass in Box 6 with the doll in Box 5.
boxes[6].remove('grass')
boxes[5].remove('doll')
boxes[6].append('doll')
boxes[5].append('grass')

# Move the skirt from Box 0 to Box 5.
boxes[0].remove('skirt')
boxes[5].append('skirt')

# Remove the umbrella from Box 6.
boxes[6].remove('umbrella')

# Move the bag from Box 8 to Box 5.
boxes[8].remove('bag')
boxes[5].append('bag')

# Put the brush and the game into Box 6.
boxes[6].append('brush')
boxes[6].append('game')

# Remove the coat and the basket and the skirt from Box 5.
items_to_remove = ['coat', 'basket', 'skirt']
for item in items_to_remove:
    boxes[5].remove(item)

# Replace the needle with the card in Box 1.
boxes[1].remove('needle')
boxes[1].append('card')

# Move the glasses and the mask and the tree from Box 3 to Box 4.
items_to_move = ['glasses', 'mask', 'tree']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Move the grass from Box 5 to Box 1.
boxes[5].remove('grass')
boxes[1].append('grass')

# Swap the tree in Box 4 with the doll in Box 6.
boxes[4].remove('tree')
boxes[6].remove('doll')
boxes[4].append('doll')
boxes[6].append('tree')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")