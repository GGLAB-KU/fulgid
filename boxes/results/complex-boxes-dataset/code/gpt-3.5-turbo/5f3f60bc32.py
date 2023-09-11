# Initial state of boxes
boxes = {
    0: ['plane', 'jungle', 'pen'],
    1: ['comet'],
    2: [],
    3: []
}

# Put the helmet into Box 1.
boxes[1].append('helmet')

# Move the helmet from Box 1 to Box 0.
boxes[1].remove('helmet')
boxes[0].append('helmet')

# Put the shoes and the laptop into Box 0.
boxes[0].append('shoes')
boxes[0].append('laptop')

# Empty Box 1.
boxes[1] = []

# Put the harmonica and the cloud into Box 0.
boxes[0].append('harmonica')
boxes[0].append('cloud')

# Move the plane and the shoes from Box 0 to Box 1.
boxes[0].remove('plane')
boxes[0].remove('shoes')
boxes[1].append('plane')
boxes[1].append('shoes')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")