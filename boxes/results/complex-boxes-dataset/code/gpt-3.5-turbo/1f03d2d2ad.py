# Initial state of boxes
boxes = {
    0: ['crown', 'car'],
    1: ['whistle', 'cup', 'ring'],
    2: ['gloves', 'button', 'fork', 'dice', 'drum'],
    3: ['plate', 'tape', 'tiger'],
    4: ['seaweed']
}

# Move the plate and the tiger and the tape from Box 3 to Box 1.
items_to_move = ['plate', 'tiger', 'tape']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[1].append(item)

# Move the car and the crown from Box 0 to Box 2.
items_to_move = ['car', 'crown']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[2].append(item)

# Remove the ring and the tape and the tiger from Box 1.
items_to_remove = ['ring', 'tape', 'tiger']
for item in items_to_remove:
    boxes[1].remove(item)

# Put the motorcycle into Box 2.
boxes[2].append('motorcycle')

# Put the motorcycle and the whistle into Box 3.
items_to_move = ['motorcycle', 'whistle']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[3].append(item)

# Move the cup from Box 1 to Box 0.
boxes[1].remove('cup')
boxes[0].append('cup')

# Move the seaweed from Box 4 to Box 1.
boxes[4].remove('seaweed')
boxes[1].append('seaweed')

# Move the cup from Box 0 to Box 3.
boxes[0].remove('cup')
boxes[3].append('cup')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")