# Initial state of boxes
boxes = {
    0: [],
    1: ['needle', 'ring', 'boot'],
    2: ['book'],
    3: ['bracelet', 'thread', 'whistle'],
    4: [],
    5: ['beach', 'octopus', 'plate', 'toy'],
    6: ['blanket', 'shampoo', 'scarf']
}

# Move the octopus and the toy and the plate from Box 5 to Box 4.
items_to_move = ['octopus', 'toy', 'plate']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Put the ocean into Box 5.
boxes[5].append('ocean')

# Empty Box 5.
boxes[5] = []

# Replace the thread and the bracelet with the ocean and the note in Box 3.
boxes[3].remove('thread')
boxes[3].remove('bracelet')
boxes[3].append('ocean')
boxes[3].append('note')

# Put the belt into Box 6.
boxes[6].append('belt')

# Empty Box 3.
boxes[3] = []

# Move the belt and the shampoo from Box 6 to Box 1.
items_to_move = ['belt', 'shampoo']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[1].append(item)

# Replace the book with the bell in Box 2.
boxes[2].remove('book')
boxes[2].append('bell')

# Put the razor and the shoe into Box 4.
boxes[4].append('razor')
boxes[4].append('shoe')

# Remove the shoe and the plate and the toy from Box 4.
items_to_remove = ['shoe', 'plate', 'toy']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the blanket and the scarf from Box 6 to Box 4.
items_to_move = ['blanket', 'scarf']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[4].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")