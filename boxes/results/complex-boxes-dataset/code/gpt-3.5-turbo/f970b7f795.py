# Initial state of boxes
boxes = {
    0: ['puzzle'],
    1: [],
    2: ['submarine'],
    3: ['elephant', 'boot', 'bag', 'zipper'],
    4: [],
    5: [],
    6: ['grinder', 'perfume', 'button', 'river', 'coat'],
    7: ['rock', 'lion'],
    8: ['speaker', 'car', 'glove', 'train']
}

# Replace the elephant and the bag with the desert and the shampoo in Box 3.
boxes[3].remove('elephant')
boxes[3].remove('bag')
boxes[3].append('desert')
boxes[3].append('shampoo')

# Move the car from Box 8 to Box 1.
boxes[8].remove('car')
boxes[1].append('car')

# Remove the submarine from Box 2.
boxes[2].remove('submarine')

# Swap the perfume in Box 6 with the puzzle in Box 0.
boxes[6].remove('perfume')
boxes[0].remove('puzzle')
boxes[6].append('puzzle')
boxes[0].append('perfume')

# Swap the shampoo in Box 3 with the lion in Box 7.
boxes[3].remove('shampoo')
boxes[7].remove('lion')
boxes[3].append('lion')
boxes[7].append('shampoo')

# Move the puzzle and the grinder from Box 6 to Box 5.
items_to_move = ['puzzle', 'grinder']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Put the river into Box 3.
boxes[6].remove('river')
boxes[3].append('river')

# Replace the puzzle with the piano in Box 5.
boxes[5].remove('puzzle')
boxes[5].append('piano')

# Empty Box 7.
boxes[7] = []

# Move the glove and the train and the speaker from Box 8 to Box 5.
items_to_move = ['glove', 'train', 'speaker']
for item in items_to_move:
    boxes[8].remove(item)
    boxes[5].append(item)

# Put the coral into Box 8.
boxes[8].append('coral')

# Remove the desert and the zipper and the boot from Box 3.
items_to_remove = ['desert', 'zipper', 'boot']
for item in items_to_remove:
    boxes[3].remove(item)

# Swap the river in Box 6 with the car in Box 1.
boxes[6].remove('river')
boxes[1].remove('car')
boxes[6].append('car')
boxes[1].append('river')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")