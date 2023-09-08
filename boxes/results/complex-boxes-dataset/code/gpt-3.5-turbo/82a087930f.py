# Initial state of boxes
boxes = {
    0: ['cow'],
    1: ['watch', 'bus', 'lipstick', 'truck', 'jacket'],
    2: ['soap'],
    3: ['console', 'pants', 'train', 'bell'],
    4: ['blender']
}

# Put the glove and the controller and the umbrella into Box 0.
items_to_add = ['glove', 'controller', 'umbrella']
for item in items_to_add:
    boxes[0].append(item)

# Empty Box 4.
boxes[4] = []

# Move the umbrella from Box 0 to Box 2.
boxes[0].remove('umbrella')
boxes[2].append('umbrella')

# Move the lipstick and the bus and the truck from Box 1 to Box 3.
items_to_move = ['lipstick', 'bus', 'truck']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[3].append(item)

# Replace the soap and the umbrella with the towel and the puzzle in Box 2.
boxes[2].remove('soap')
boxes[2].remove('umbrella')
boxes[2].append('towel')
boxes[2].append('puzzle')

# Swap the jacket in Box 1 with the puzzle in Box 2.
boxes[1].remove('jacket')
boxes[2].remove('puzzle')
boxes[1].append('puzzle')
boxes[2].append('jacket')

# Put the coin and the mask into Box 4.
items_to_add = ['coin', 'mask']
for item in items_to_add:
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")