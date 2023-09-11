# Initial state of boxes
boxes = {
    0: ['snow', 'ring'],
    1: ['bear', 'motorcycle', 'beach', 'game', 'frame'],
    2: [],
    3: ['grass', 'umbrella', 'shark', 'headphone', 'bus']
}

# Move the ring from Box 0 to Box 2.
boxes[0].remove('ring')
boxes[2].append('ring')

# Move the snow from Box 0 to Box 2.
boxes[0].remove('snow')
boxes[2].append('snow')

# Move the shark and the grass and the headphone from Box 3 to Box 1.
items_to_move = ['shark', 'grass', 'headphone']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Empty Box 2.
boxes[2] = []

# Swap the umbrella in Box 3 with the game in Box 1.
boxes[3].remove('umbrella')
boxes[1].remove('game')
boxes[3].append('game')
boxes[1].append('umbrella')

# Move the game and the bus from Box 3 to Box 0.
items_to_move = ['game', 'bus']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")