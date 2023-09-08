# Initial state of boxes
boxes = {
    0: ['ship', 'pen', 'tie', 'snow', 'tiger'],
    1: ['violin', 'truck'],
    2: [],
    3: [],
    4: ['toothpaste', 'microwave', 'jungle', 'perfume'],
    5: ['blender', 'glove']
}

# Remove the pen and the snow and the tiger from Box 0.
items_to_remove = ['pen', 'snow', 'tiger']
for item in items_to_remove:
    boxes[0].remove(item)

# Move the glove and the blender from Box 5 to Box 4.
items_to_move = ['glove', 'blender']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Move the tie from Box 0 to Box 5.
boxes[0].remove('tie')
boxes[5].append('tie')

# Remove the microwave and the perfume and the jungle from Box 4.
items_to_remove = ['microwave', 'perfume', 'jungle']
for item in items_to_remove:
    boxes[4].remove(item)

# Move the toothpaste from Box 4 to Box 5.
boxes[4].remove('toothpaste')
boxes[5].append('toothpaste')

# Put the charger and the oven into Box 3.
boxes[3].append('charger')
boxes[3].append('oven')

# Move the toothpaste from Box 5 to Box 1.
boxes[5].remove('toothpaste')
boxes[1].append('toothpaste')

# Swap the oven in Box 3 with the glove in Box 4.
boxes[3].remove('oven')
boxes[4].remove('glove')
boxes[3].append('glove')
boxes[4].append('oven')

# Move the glove from Box 3 to Box 4.
boxes[3].remove('glove')
boxes[4].append('glove')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")