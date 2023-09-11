# Initial state of boxes
boxes = {
    0: ['gloves', 'horse', 'pen', 'fish'],
    1: ['candle', 'speaker'],
    2: ['dice'],
    3: ['pillow', 'lightning'],
    4: ['blanket', 'vase', 'basket', 'jacket'],
    5: [],
    6: ['cup', 'pot', 'thread', 'needle']
}

# Move the thread from Box 6 to Box 1.
boxes[6].remove('thread')
boxes[1].append('thread')

# Move the candle and the speaker from Box 1 to Box 4.
items_to_move = ['candle', 'speaker']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[4].append(item)

# Remove the pillow from Box 3.
boxes[3].remove('pillow')

# Swap the dice in Box 2 with the lightning in Box 3.
boxes[2].remove('dice')
boxes[3].remove('lightning')
boxes[2].append('lightning')
boxes[3].append('dice')

# Replace the dice with the ship in Box 3.
boxes[3].remove('dice')
boxes[3].append('ship')

# Swap the ship in Box 3 with the pot in Box 6.
boxes[3].remove('ship')
boxes[6].remove('pot')
boxes[3].append('pot')
boxes[6].append('ship')

# Remove the lightning from Box 2.
boxes[2].remove('lightning')

# Put the blanket and the skirt and the cloud into Box 5.
items_to_move = ['blanket', 'skirt', 'cloud']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Replace the fish with the scarf in Box 0.
boxes[0].remove('fish')
boxes[0].append('scarf')

# Remove the cloud from Box 5.
boxes[5].remove('cloud')

# Replace the thread with the sandals in Box 1.
boxes[1].remove('thread')
boxes[1].append('sandals')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")