# Initial state of boxes
boxes = {
    0: ['zipper'],
    1: ['shoes', 'doll', 'dog'],
    2: [],
    3: ['flute', 'plate', 'toaster'],
    4: [],
    5: ['violin', 'elephant', 'comb']
}

# Replace the zipper with the chair in Box 0.
boxes[0].remove('zipper')
boxes[0].append('chair')

# Put the charger and the toaster and the pan into Box 5.
boxes[5].append('charger')
boxes[5].append('toaster')
boxes[5].append('pan')

# Remove the shoes and the dog and the doll from Box 1.
boxes[1].remove('shoes')
boxes[1].remove('dog')
boxes[1].remove('doll')

# Empty Box 3.
boxes[3] = []

# Put the piano into Box 3.
boxes[3].append('piano')

# Remove the piano from Box 3.
boxes[3].remove('piano')

# Swap the chair in Box 0 with the charger in Box 5.
boxes[0].remove('chair')
boxes[5].remove('charger')
boxes[0].append('charger')
boxes[5].append('chair')

# Move the pan and the toaster and the comb from Box 5 to Box 2.
items_to_move = ['pan', 'toaster', 'comb']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[2].append(item)

# Move the violin and the chair from Box 5 to Box 3.
items_to_move = ['violin', 'chair']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")