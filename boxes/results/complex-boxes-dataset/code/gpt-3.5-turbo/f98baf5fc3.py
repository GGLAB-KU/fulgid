# Initial state of boxes
boxes = {
    0: ['jungle', 'frame', 'spoon'],
    1: ['comet'],
    2: ['watch', 'makeup', 'zipper', 'toothbrush'],
    3: ['pot', 'swimsuit', 'hat', 'bell'],
    4: ['shampoo', 'bear']
}

# Remove the comet from Box 1.
boxes[1].remove('comet')

# Move the bear and the shampoo from Box 4 to Box 3.
items_to_move = ['bear', 'shampoo']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Put the keyboard and the submarine into Box 2.
items_to_add = ['keyboard', 'submarine']
for item in items_to_add:
    boxes[2].append(item)

# Put the rain and the swimsuit and the cat into Box 2.
items_to_add = ['rain', 'swimsuit', 'cat']
for item in items_to_add:
    boxes[2].append(item)

# Replace the spoon with the sun in Box 0.
boxes[0].remove('spoon')
boxes[0].append('sun')

# Put the jungle into Box 4.
boxes[4].append('jungle')

# Put the bowl into Box 4.
boxes[4].append('bowl')

# Move the jungle and the bowl from Box 4 to Box 3.
items_to_move = ['jungle', 'bowl']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")