# Initial state of boxes
boxes = {
    0: ['wire', 'bag', 'coral', 'wallet'],
    1: [],
    2: ['motorcycle', 'basket', 'controller', 'car'],
    3: ['card', 'octopus', 'zipper', 'shoe', 'desert'],
    4: ['shampoo', 'note', 'game', 'table'],
    5: ['lightning', 'thread', 'toothbrush'],
    6: [],
    7: [],
    8: ['freezer', 'bell', 'speaker', 'scarf', 'dress']
}

# Remove the shampoo and the table and the note from Box 4.
boxes[4].remove('shampoo')
boxes[4].remove('table')
boxes[4].remove('note')

# Replace the bag with the sock in Box 0.
boxes[0].remove('bag')
boxes[0].append('sock')

# Swap the wire in Box 0 with the motorcycle in Box 2.
boxes[0].remove('wire')
boxes[2].remove('motorcycle')
boxes[0].append('motorcycle')
boxes[2].append('wire')

# Move the scarf and the speaker and the bell from Box 8 to Box 7.
items_to_move = ['scarf', 'speaker', 'bell']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[7].append(item)

# Put the starfish and the rain and the tree into Box 6.
items_to_put = ['starfish', 'rain', 'tree']
for item in items_to_put:
    boxes[6].append(item)

# Put the lipstick and the thread into Box 2.
items_to_put = ['lipstick', 'thread']
for item in items_to_put:
    boxes[2].append(item)

# Put the toaster into Box 0.
boxes[0].append('toaster')

# Swap the desert in Box 3 with the game in Box 4.
boxes[3].remove('desert')
boxes[4].remove('game')
boxes[3].append('game')
boxes[4].append('desert')

# Move the wire and the car from Box 2 to Box 7.
items_to_move = ['wire', 'car']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[7].append(item)

# Swap the lipstick in Box 2 with the desert in Box 4.
boxes[2].remove('lipstick')
boxes[4].remove('desert')
boxes[2].append('desert')
boxes[4].append('lipstick')

# Replace the thread and the controller and the basket with the pan and the toy and the branch in Box 2.
items_to_remove = ['thread', 'controller', 'basket']
items_to_add = ['pan', 'toy', 'branch']
for item in items_to_remove:
    boxes[2].remove(item)
for item in items_to_add:
    boxes[2].append(item)

# Replace the freezer with the dress in Box 8.
boxes[8].remove('freezer')
boxes[8].append('dress')

# Put the puzzle and the blender into Box 3.
items_to_put = ['puzzle', 'blender']
for item in items_to_put:
    boxes[3].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")