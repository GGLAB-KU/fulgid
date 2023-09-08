# Initial state of boxes
boxes = {
    0: [],
    1: ['grinder', 'book'],
    2: ['razor'],
    3: ['doll', 'mountain', 'freezer'],
    4: [],
    5: []
}

# Swap the mountain in Box 3 with the razor in Box 2.
boxes[3].remove('mountain')
boxes[2].remove('razor')
boxes[3].append('razor')
boxes[2].append('mountain')

# Put the shoe and the bag into Box 0.
boxes[0].append('shoe')
boxes[0].append('bag')

# Move the doll from Box 3 to Box 1.
boxes[3].remove('doll')
boxes[1].append('doll')

# Move the razor and the freezer from Box 3 to Box 2.
boxes[3].remove('razor')
boxes[3].remove('freezer')
boxes[2].append('razor')
boxes[2].append('freezer')

# Remove the book and the doll and the grinder from Box 1.
items_to_remove = ['book', 'doll', 'grinder']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the mountain in Box 2 with the bag in Box 0.
boxes[2].remove('mountain')
boxes[0].remove('bag')
boxes[2].append('bag')
boxes[0].append('mountain')

# Swap the mountain in Box 0 with the freezer in Box 2.
boxes[0].remove('mountain')
boxes[2].remove('freezer')
boxes[0].append('freezer')
boxes[2].append('mountain')

# Remove the shoe from Box 0.
boxes[0].remove('shoe')

# Swap the razor in Box 2 with the freezer in Box 0.
boxes[2].remove('razor')
boxes[0].remove('freezer')
boxes[2].append('freezer')
boxes[0].append('razor')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")