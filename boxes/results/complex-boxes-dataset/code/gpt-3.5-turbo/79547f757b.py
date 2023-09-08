# Initial state of boxes
boxes = {
    0: ['glove'],
    1: ['boot', 'forest', 'bell'],
    2: ['wig', 'motorcycle', 'scarf'],
    3: ['island'],
    4: ['ocean', 'vase', 'toy']
}

# Put the rain and the mountain into Box 2.
boxes[2].append('rain')
boxes[2].append('mountain')

# Move the rain and the scarf and the mountain from Box 2 to Box 1.
items_to_move = ['rain', 'scarf', 'mountain']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[1].append(item)

# Move the ocean and the vase from Box 4 to Box 2.
items_to_move = ['ocean', 'vase']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[2].append(item)

# Remove the glove from Box 0.
boxes[0].remove('glove')

# Replace the toy with the butterfly in Box 4.
boxes[4].remove('toy')
boxes[4].append('butterfly')

# Put the sock into Box 2.
boxes[2].append('sock')

# Replace the island with the earring in Box 3.
boxes[3].remove('island')
boxes[3].append('earring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")