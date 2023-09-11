# Initial state of boxes
boxes = {
    0: [],
    1: ['coral', 'river', 'cup'],
    2: [],
    3: ['bracelet', 'key', 'lock', 'bowl']
}

# Move the river from Box 1 to Box 0.
boxes[0].append(boxes[1].pop(boxes[1].index('river')))

# Put the toy into Box 0.
boxes[0].append('toy')

# Put the boot and the watch and the bus into Box 3.
boxes[3].extend(['boot', 'watch', 'bus'])

# Put the fish and the beach and the fridge into Box 2.
boxes[2].extend(['fish', 'beach', 'fridge'])

# Replace the cup and the coral with the toothbrush and the coat in Box 1.
boxes[1].remove('cup')
boxes[1].remove('coral')
boxes[1].extend(['toothbrush', 'coat'])

# Put the dress and the crown into Box 1.
boxes[1].extend(['dress', 'crown'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")