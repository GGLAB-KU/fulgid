# Initial state of boxes
boxes = {
    0: ['dog', 'vase', 'candle', 'shampoo', 'speaker'],
    1: ['dress'],
    2: ['tiger', 'scarf', 'polish'],
    3: ['microwave'],
    4: ['card', 'lock'],
    5: []
}

# Swap the microwave in Box 3 with the tiger in Box 2.
boxes[3], boxes[2] = boxes[2], boxes[3]

# Remove the shampoo from Box 0.
boxes[0].remove('shampoo')

# Empty Box 3.
boxes[3] = []

# Move the vase from Box 0 to Box 2.
boxes[0].remove('vase')
boxes[2].append('vase')

# Move the dog from Box 0 to Box 4.
boxes[0].remove('dog')
boxes[4].append('dog')

# Put the magnet and the headphone into Box 4.
boxes[4].extend(['magnet', 'headphone'])

# Swap the dress in Box 1 with the microwave in Box 2.
boxes[1], boxes[2] = boxes[2], boxes[1]

# Swap the vase in Box 2 with the microwave in Box 1.
boxes[2], boxes[1] = boxes[1], boxes[2]

# Put the scissors and the scarf into Box 1.
boxes[1].extend(['scissors', 'scarf'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")