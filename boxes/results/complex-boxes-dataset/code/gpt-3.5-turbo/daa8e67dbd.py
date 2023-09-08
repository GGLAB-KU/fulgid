# Initial state of boxes
boxes = {
    0: ['ring', 'pen', 'earring'],
    1: [],
    2: ['coral', 'chair'],
    3: ['towel', 'lion', 'thread', 'ocean'],
    4: []
}

# Move the towel and the ocean and the lion from Box 3 to Box 0.
items_to_move = ['towel', 'ocean', 'lion']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[0].append(item)

# Remove the coral and the chair from Box 2.
boxes[2].remove('coral')
boxes[2].remove('chair')

# Empty Box 3.
boxes[3] = []

# Remove the earring and the pen from Box 0.
boxes[0].remove('earring')
boxes[0].remove('pen')

# Move the lion and the towel and the ocean from Box 0 to Box 4.
items_to_move = ['lion', 'towel', 'ocean']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Move the ring from Box 0 to Box 2.
boxes[0].remove('ring')
boxes[2].append('ring')

# Remove the ring from Box 2.
boxes[2].remove('ring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")