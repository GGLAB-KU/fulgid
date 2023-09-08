# Initial state of boxes
boxes = {
    0: ['hat', 'lamp', 'sock', 'storm'],
    1: ['zipper', 'desert'],
    2: ['bowl', 'freezer', 'jungle'],
    3: ['belt', 'game'],
    4: ['charger'],
    5: [],
    6: ['scissors'],
    7: ['dog', 'pot', 'grinder'],
    8: ['lion', 'forest', 'sandals', 'speaker', 'crown'],
    9: ['razor'],
    10: [],
    11: ['clock'],
    12: []
}

# Move the dog from Box 7 to Box 10.
boxes[7].remove('dog')
boxes[10].append('dog')

# Put the coral into Box 12.
boxes[12].append('coral')

# Move the charger from Box 4 to Box 6.
boxes[4].remove('charger')
boxes[6].append('charger')

# Put the plate into Box 5.
boxes[5].append('plate')

# Put the keyboard and the coral and the shirt into Box 0.
items_to_move = ['keyboard', 'coral', 'shirt']
for item in items_to_move:
    boxes[0].append(item)

# Move the sandals and the forest from Box 8 to Box 3.
items_to_move = ['sandals', 'forest']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[3].append(item)

# Move the jungle and the freezer and the bowl from Box 2 to Box 9.
items_to_move = ['jungle', 'freezer', 'bowl']
for item in items_to_move:
    boxes[2].remove(item)
    boxes[9].append(item)

# Remove the zipper from Box 1.
boxes[1].remove('zipper')

# Put the fish and the phone into Box 10.
items_to_move = ['fish', 'phone']
for item in items_to_move:
    boxes[10].append(item)

# Replace the shirt and the storm with the jungle and the island in Box 0.
boxes[0].remove('shirt')
boxes[0].remove('storm')
boxes[0].append('jungle')
boxes[0].append('island')

# Put the toothbrush and the helmet into Box 7.
items_to_move = ['toothbrush', 'helmet']
for item in items_to_move:
    boxes[7].append(item)

# Put the mountain into Box 1.
boxes[1].append('mountain')

# Put the shark and the mountain and the soap into Box 12.
items_to_move = ['shark', 'mountain', 'soap']
for item in items_to_move:
    boxes[12].append(item)

# Put the jungle and the tape into Box 4.
items_to_move = ['jungle', 'tape']
for item in items_to_move:
    boxes[4].append(item)

# Put the vase and the dice into Box 10.
items_to_move = ['vase', 'dice']
for item in items_to_move:
    boxes[10].append(item)

# Swap the game in Box 3 with the jungle in Box 4.
boxes[3].remove('game')
boxes[4].remove('jungle')
boxes[3].append('jungle')
boxes[4].append('game')

# Replace the charger with the keyboard in Box 6.
boxes[6].remove('charger')
boxes[6].append('keyboard')

# Put the cat into Box 4.
boxes[4].append('cat')

# Put the hat and the rock into Box 1.
items_to_move = ['hat', 'rock']
for item in items_to_move:
    boxes[1].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")