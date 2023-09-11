# Initial state of boxes
boxes = {
    0: ['plane'],
    1: [],
    2: ['key', 'grinder', 'phone'],
    3: ['oven', 'doll']
}

# Empty Box 3
boxes[3] = []

# Put the book and the helmet and the thunder into Box 2
boxes[2].append('book')
boxes[2].append('helmet')
boxes[2].append('thunder')

# Swap the phone in Box 2 with the plane in Box 0
boxes[0], boxes[2] = boxes[2], boxes[0]

# Remove the phone from Box 0
boxes[0].remove('phone')

# Remove the key and the thunder from Box 2
boxes[2].remove('key')
boxes[2].remove('thunder')

# Remove the book and the plane from Box 2
boxes[2].remove('book')
boxes[2].remove('plane')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")