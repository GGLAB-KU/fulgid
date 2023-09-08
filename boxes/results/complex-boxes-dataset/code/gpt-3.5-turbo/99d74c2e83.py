# Initial state of boxes
boxes = {
    0: ['polish', 'zipper'],
    1: ['blender', 'rock', 'bowl'],
    2: ['glasses', 'vase', 'pants'],
    3: ['wallet', 'submarine', 'cloud', 'dice', 'phone'],
    4: []
}

# Swap the dice in Box 3 with the rock in Box 1.
boxes[3].remove('dice')
boxes[1].remove('rock')
boxes[3].append('rock')
boxes[1].append('dice')

# Swap the glasses in Box 2 with the wallet in Box 3.
boxes[2].remove('glasses')
boxes[3].remove('wallet')
boxes[2].append('wallet')
boxes[3].append('glasses')

# Move the glasses and the cloud and the submarine from Box 3 to Box 0.
items_to_move = ['glasses', 'cloud', 'submarine']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Remove the wallet from Box 2.
boxes[2].remove('wallet')

# Replace the glasses and the polish and the submarine with the candle and the glove and the pants in Box 0.
boxes[0].remove('glasses')
boxes[0].remove('polish')
boxes[0].remove('submarine')
boxes[0].append('candle')
boxes[0].append('glove')
boxes[0].append('pants')

# Put the vase and the mask into Box 3.
boxes[3].append('vase')
boxes[3].append('mask')

# Move the vase from Box 3 to Box 4.
boxes[3].remove('vase')
boxes[4].append('vase')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")