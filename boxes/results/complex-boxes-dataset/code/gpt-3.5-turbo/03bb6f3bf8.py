# Initial state of boxes
boxes = {
    0: ['chair', 'note'],
    1: [],
    2: [],
    3: ['pan', 'pen', 'bicycle']
}

# Empty Box 3
boxes[3] = []

# Empty Box 0
boxes[0] = []

# Put the brush and the bird and the star into Box 0
items_to_put = ['brush', 'bird', 'star']
boxes[0].extend(items_to_put)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")