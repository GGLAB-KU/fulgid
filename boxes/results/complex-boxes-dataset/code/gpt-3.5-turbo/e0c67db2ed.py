# Initial state of boxes
boxes = {
    0: ['camera'],
    1: ['magnet', 'microscope', 'apple', 'scissors'],
    2: [],
    3: ['horn', 'speaker'],
    4: ['beach', 'wig', 'spoon', 'mountain'],
    5: ['button', 'coat', 'polish']
}

# Move the button from Box 5 to Box 1.
boxes[5].remove('button')
boxes[1].append('button')

# Move the wig and the beach from Box 4 to Box 5.
items_to_move = ['wig', 'beach']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[5].append(item)

# Move the camera from Box 0 to Box 5.
boxes[0].remove('camera')
boxes[5].append('camera')

# Move the mountain from Box 4 to Box 5.
boxes[4].remove('mountain')
boxes[5].append('mountain')

# Put the boot and the spoon into Box 0.
items_to_put = ['boot', 'spoon']
for item in items_to_put:
    boxes[0].append(item)

# Put the piano and the oven and the rain into Box 3.
items_to_put = ['piano', 'oven', 'rain']
for item in items_to_put:
    boxes[3].append(item)

# Put the keyboard and the shoe into Box 0.
items_to_put = ['keyboard', 'shoe']
for item in items_to_put:
    boxes[0].append(item)

# Swap the spoon in Box 4 with the oven in Box 3.
boxes[4].remove('spoon')
boxes[3].remove('oven')
boxes[4].append('oven')
boxes[3].append('spoon')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")