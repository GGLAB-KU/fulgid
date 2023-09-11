# Initial state of boxes
boxes = {
    0: ['bus'],
    1: ['train', 'polish', 'tiger', 'table', 'toothpaste'],
    2: ['bowl', 'microscope', 'game', 'wallet'],
    3: ['dolphin', 'shelf', 'thread', 'toothbrush'],
    4: []
}

# Swap the bus in Box 0 with the microscope in Box 2.
boxes[0], boxes[2] = boxes[2], boxes[0]

# Move the microscope from Box 0 to Box 1.
boxes[0].remove('microscope')
boxes[1].append('microscope')

# Put the keyboard and the button into Box 2.
boxes[2].append('keyboard')
boxes[2].append('button')

# Move the thread and the dolphin from Box 3 to Box 1.
boxes[3].remove('thread')
boxes[3].remove('dolphin')
boxes[1].append('thread')
boxes[1].append('dolphin')

# Swap the keyboard in Box 2 with the toothbrush in Box 3.
boxes[2].remove('keyboard')
boxes[3].remove('toothbrush')
boxes[2].append('toothbrush')
boxes[3].append('keyboard')

# Move the game from Box 2 to Box 4.
boxes[2].remove('game')
boxes[4].append('game')

# Replace the button with the jungle in Box 2.
boxes[2].remove('button')
boxes[2].append('jungle')

# Remove the microscope and the polish and the tiger from Box 1.
items_to_remove = ['microscope', 'polish', 'tiger']
for item in items_to_remove:
    boxes[1].remove(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")