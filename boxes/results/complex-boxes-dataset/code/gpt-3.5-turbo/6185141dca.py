# Initial state of boxes
boxes = {
    0: ['cup', 'jacket'],
    1: ['sandals', 'shorts', 'perfume', 'ring'],
    2: ['cloud', 'tiger', 'island'],
    3: ['piano', 'scarf'],
    4: ['toy', 'violin', 'fish', 'zipper'],
    5: ['bus', 'train'],
    6: ['thread', 'blanket', 'plate']
}

# Remove the blanket and the thread from Box 6.
boxes[6].remove('blanket')
boxes[6].remove('thread')

# Move the island from Box 2 to Box 0.
boxes[0].append(boxes[2].pop(boxes[2].index('island')))

# Put the octopus and the pot into Box 2.
boxes[2].extend(['octopus', 'pot'])

# Swap the toy in Box 4 with the ring in Box 1.
boxes[4].remove('toy')
boxes[1].remove('ring')
boxes[4].append('ring')
boxes[1].append('toy')

# Remove the octopus and the pot and the tiger from Box 2.
items_to_remove = ['octopus', 'pot', 'tiger']
for item in items_to_remove:
    boxes[2].remove(item)

# Put the bird and the cup and the tree into Box 3.
boxes[3].extend(['bird', 'cup', 'tree'])

# Remove the train from Box 5.
boxes[5].remove('train')

# Replace the cloud with the pants in Box 2.
boxes[2].remove('cloud')
boxes[2].append('pants')

# Swap the cup in Box 3 with the violin in Box 4.
boxes[3].remove('cup')
boxes[4].remove('violin')
boxes[3].append('violin')
boxes[4].append('cup')

# Swap the shorts in Box 1 with the plate in Box 6.
boxes[1].remove('shorts')
boxes[6].remove('plate')
boxes[1].append('plate')
boxes[6].append('shorts')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")