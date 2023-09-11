# Initial state of boxes
boxes = {
    0: [],
    1: ['paint', 'pillow'],
    2: [],
    3: ['pot', 'towel', 'freezer', 'whistle']
}

# Swap the pillow in Box 1 with the freezer in Box 3.
boxes[1].remove('pillow')
boxes[3].remove('freezer')
boxes[1].append('freezer')
boxes[3].append('pillow')

# Move the towel and the pot and the whistle from Box 3 to Box 0.
items_to_move = ['towel', 'pot', 'whistle']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Empty Box 0.
boxes[0] = []

# Move the pillow from Box 3 to Box 2.
boxes[3].remove('pillow')
boxes[2].append('pillow')

# Remove the paint from Box 1.
boxes[1].remove('paint')

# Move the freezer from Box 1 to Box 2.
boxes[1].remove('freezer')
boxes[2].append('freezer')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")