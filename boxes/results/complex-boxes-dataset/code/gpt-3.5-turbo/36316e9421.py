# Initial state of boxes
boxes = {
    0: ['toothbrush'],
    1: ['toy', 'ocean'],
    2: ['elephant', 'gloves', 'horse', 'tiger', 'needle'],
    3: ['desert']
}

# Move the desert from Box 3 to Box 0.
boxes[0].append(boxes[3].pop())

# Remove the toothbrush from Box 0.
boxes[0].remove('toothbrush')

# Remove the ocean and the toy from Box 1.
boxes[1].remove('ocean')
boxes[1].remove('toy')

# Move the desert from Box 0 to Box 3.
boxes[3].append(boxes[0].pop())

# Move the desert from Box 3 to Box 0.
boxes[0].append(boxes[3].pop())

# Replace the elephant with the fish in Box 2.
boxes[2].remove('elephant')
boxes[2].append('fish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")