# Initial state of boxes
boxes = {
    0: [],
    1: ['plate', 'drum', 'telescope', 'cow'],
    2: ['tape', 'blender', 'ocean', 'key'],
    3: ['lightning'],
    4: ['sock', 'flower', 'camera', 'river', 'island'],
    5: ['pants'],
    6: ['gloves', 'coral', 'table'],
    7: ['meteor', 'brush', 'charger', 'scissors'],
    8: ['card', 'mask', 'tiger', 'submarine']
}

# Put the motorcycle and the forest and the shampoo into Box 3.
boxes[3].extend(['motorcycle', 'forest', 'shampoo'])

# Put the glove into Box 2.
boxes[2].append('glove')

# Swap the charger in Box 7 with the submarine in Box 8.
boxes[7].remove('charger')
boxes[8].remove('submarine')
boxes[7].append('submarine')
boxes[8].append('charger')

# Move the shampoo and the forest and the motorcycle from Box 3 to Box 2.
items_to_move = ['shampoo', 'forest', 'motorcycle']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[2].append(item)

# Put the spoon and the cow and the charger into Box 2.
boxes[2].extend(['spoon', 'cow', 'charger'])

# Put the apple and the button into Box 4.
boxes[4].extend(['apple', 'button'])

# Move the table and the gloves from Box 6 to Box 5.
items_to_move = ['table', 'gloves']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Put the lock into Box 0.
boxes[0].append('lock')

# Swap the plate in Box 1 with the flower in Box 4.
boxes[1].remove('plate')
boxes[4].remove('flower')
boxes[1].append('flower')
boxes[4].append('plate')

# Move the drum and the flower from Box 1 to Box 2.
items_to_move = ['drum', 'flower']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[2].append(item)

# Move the meteor and the submarine and the scissors from Box 7 to Box 6.
items_to_move = ['meteor', 'submarine', 'scissors']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[6].append(item)

# Put the puzzle and the frame into Box 2.
boxes[2].extend(['puzzle', 'frame'])

# Empty Box 0.
boxes[0] = []

# Put the laptop and the belt into Box 6.
boxes[6].extend(['laptop', 'belt'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")