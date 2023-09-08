# Initial state of boxes
boxes = {
    0: ['zipper'],
    1: ['hat', 'needle'],
    2: ['towel', 'plate'],
    3: [],
    4: ['button', 'storm', 'card']
}

# Replace the zipper with the belt in Box 0.
boxes[0].remove('zipper')
boxes[0].append('belt')

# Move the needle from Box 1 to Box 3.
boxes[1].remove('needle')
boxes[3].append('needle')

# Put the keyboard into Box 4.
boxes[4].append('keyboard')

# Put the shampoo and the bicycle and the pants into Box 3.
items_to_move = ['shampoo', 'bicycle', 'pants']
for item in items_to_move:
    boxes[3].append(item)

# Replace the card and the storm with the rock and the octopus in Box 4.
boxes[4].remove('card')
boxes[4].remove('storm')
boxes[4].append('rock')
boxes[4].append('octopus')

# Swap the towel in Box 2 with the hat in Box 1.
boxes[1].remove('hat')
boxes[2].remove('towel')
boxes[1].append('towel')
boxes[2].append('hat')

# Remove the belt from Box 0.
boxes[0].remove('belt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")