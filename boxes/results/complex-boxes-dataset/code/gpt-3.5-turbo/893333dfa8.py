# Initial state of boxes
boxes = {
    0: ['toy', 'beach'],
    1: ['charger'],
    2: ['console', 'battery'],
    3: []
}

# Move the battery and the console from Box 2 to Box 0.
boxes[0].extend(boxes[2])
boxes[2] = []

# Move the console from Box 0 to Box 1.
boxes[1].append(boxes[0].pop(1))

# Replace the beach and the battery and the toy with the sculpture and the desert and the ring in Box 0.
boxes[0].remove('beach')
boxes[0].remove('battery')
boxes[0].remove('toy')
boxes[0].extend(['sculpture', 'desert', 'ring'])

# Swap the desert in Box 0 with the charger in Box 1.
boxes[0][1], boxes[1][0] = boxes[1][0], boxes[0][1]

# Replace the ring with the basket in Box 0.
boxes[0].remove('ring')
boxes[0].append('basket')

# Replace the basket and the charger with the flower and the microscope in Box 0.
boxes[0].remove('basket')
boxes[0].remove('charger')
boxes[0].extend(['flower', 'microscope'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")