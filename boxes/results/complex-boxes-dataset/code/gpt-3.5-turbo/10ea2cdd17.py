# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['butterfly', 'table'],
    3: ['bracelet', 'makeup'],
    4: ['beach']
}

# Put the pillow into Box 1.
boxes[1].append('pillow')

# Replace the pillow with the vase in Box 1.
boxes[1].remove('pillow')
boxes[1].append('vase')

# Remove the beach from Box 4.
boxes[4].remove('beach')

# Put the snow into Box 1.
boxes[1].append('snow')

# Put the pen and the shirt into Box 3.
boxes[3].append('pen')
boxes[3].append('shirt')

# Swap the butterfly in Box 2 with the shirt in Box 3.
boxes[2].remove('butterfly')
boxes[3].remove('shirt')
boxes[2].append('shirt')
boxes[3].append('butterfly')

# Remove the shirt from Box 2.
boxes[2].remove('shirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")