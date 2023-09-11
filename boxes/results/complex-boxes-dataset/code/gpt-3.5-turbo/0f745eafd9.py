# Initial state of boxes
boxes = {
    0: ['headphone', 'comet', 'thunder'],
    1: ['horn', 'skirt', 'sandals'],
    2: [],
    3: ['dolphin', 'branch']
}

# Remove the dolphin from Box 3.
boxes[3].remove('dolphin')

# Replace the branch with the scissors in Box 3.
boxes[3].remove('branch')
boxes[3].append('scissors')

# Replace the scissors with the sun in Box 3.
boxes[3].remove('scissors')
boxes[3].append('sun')

# Put the puzzle and the train and the needle into Box 2.
items_to_move = ['puzzle', 'train', 'needle']
for item in items_to_move:
    boxes[2].append(item)

# Swap the thunder in Box 0 with the sun in Box 3.
boxes[0].remove('thunder')
boxes[3].remove('sun')
boxes[0].append('sun')
boxes[3].append('thunder')

# Replace the puzzle with the blender in Box 2.
boxes[2].remove('puzzle')
boxes[2].append('blender')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")