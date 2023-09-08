# Initial state of boxes
boxes = {
    0: [],
    1: ['beach', 'wallet', 'drum', 'bowl'],
    2: ['tree'],
    3: ['earring', 'cup'],
    4: []
}

# Put the chair and the rock and the watch into Box 1.
items_to_put = ['chair', 'rock', 'watch']
for item in items_to_put:
    boxes[1].append(item)

# Remove the drum from Box 1.
boxes[1].remove('drum')

# Move the tree from Box 2 to Box 4.
boxes[4].append(boxes[2].pop())

# Swap the tree in Box 4 with the cup in Box 3.
boxes[4], boxes[3] = boxes[3], boxes[4]

# Move the cup from Box 4 to Box 1.
boxes[1].append(boxes[4].pop())

# Put the ring into Box 4.
boxes[4].append('ring')

# Empty Box 4.
boxes[4] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")