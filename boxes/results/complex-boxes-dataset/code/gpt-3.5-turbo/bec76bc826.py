# Initial state of boxes
boxes = {
    0: ['chair', 'skirt'],
    1: [],
    2: ['makeup', 'needle', 'sculpture'],
    3: ['crown', 'planet', 'tree', 'star'],
    4: ['grass', 'book', 'starfish', 'sun']
}

# Replace the skirt with the shoes in Box 0.
boxes[0].remove('skirt')
boxes[0].append('shoes')

# Remove the needle and the makeup from Box 2.
boxes[2].remove('needle')
boxes[2].remove('makeup')

# Swap the shoes in Box 0 with the tree in Box 3.
boxes[0].remove('shoes')
boxes[3].remove('tree')
boxes[0].append('tree')
boxes[3].append('shoes')

# Put the shirt into Box 3.
boxes[3].append('shirt')

# Remove the sculpture from Box 2.
boxes[2].remove('sculpture')

# Replace the crown with the frame in Box 3.
boxes[3].remove('crown')
boxes[3].append('frame')

# Remove the star and the planet and the frame from Box 3.
boxes[3].remove('star')
boxes[3].remove('planet')
boxes[3].remove('frame')

# Remove the book and the grass from Box 4.
boxes[4].remove('book')
boxes[4].remove('grass')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")