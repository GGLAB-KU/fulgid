# Initial state of boxes
boxes = {
    0: [],
    1: ['snow', 'bowl', 'rocket'],
    2: ['bus'],
    3: ['cat', 'flute']
}

# Put the cloud into Box 3.
boxes[3].append('cloud')

# Put the shelf and the fish into Box 3.
boxes[3].append('shelf')
boxes[3].append('fish')

# Move the shelf and the cat from Box 3 to Box 2.
boxes[2].append(boxes[3].pop(boxes[3].index('shelf')))
boxes[2].append(boxes[3].pop(boxes[3].index('cat')))

# Swap the cat in Box 2 with the rocket in Box 1.
boxes[1].append(boxes[2].pop(boxes[2].index('cat')))
boxes[2].append(boxes[1].pop(boxes[1].index('rocket')))

# Replace the fish with the scarf in Box 3.
boxes[3].remove('fish')
boxes[3].append('scarf')

# Swap the rocket in Box 2 with the bowl in Box 1.
boxes[1].append(boxes[2].pop(boxes[2].index('rocket')))
boxes[2].append(boxes[1].pop(boxes[1].index('bowl')))

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")