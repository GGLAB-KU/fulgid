# Initial state of boxes
boxes = {
    0: ['earring', 'lion', 'polish', 'vase'],
    1: ['bear', 'starfish', 'bell'],
    2: ['bag'],
    3: ['thread'],
    4: ['elephant', 'plane', 'microscope', 'lipstick']
}

# Move the microscope and the elephant and the plane from Box 4 to Box 0.
items_to_move = ['microscope', 'elephant', 'plane']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Move the thread from Box 3 to Box 1.
boxes[3].remove('thread')
boxes[1].append('thread')

# Move the microscope and the earring and the vase from Box 0 to Box 1.
items_to_move = ['microscope', 'earring', 'vase']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[1].append(item)

# Remove the bear from Box 1.
boxes[1].remove('bear')

# Put the snow into Box 0.
boxes[0].append('snow')

# Remove the microscope and the earring and the bell from Box 1.
items_to_remove = ['microscope', 'earring', 'bell']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the lipstick in Box 4 with the lion in Box 0.
boxes[0].remove('lion')
boxes[4].remove('lipstick')
boxes[0].append('lipstick')
boxes[4].append('lion')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")