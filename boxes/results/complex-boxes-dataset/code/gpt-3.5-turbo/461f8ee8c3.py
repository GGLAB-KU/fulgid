# Initial state of boxes
boxes = {
    0: ['storm'],
    1: ['button', 'telescope'],
    2: ['rock', 'zipper'],
    3: ['blanket'],
    4: ['meteor', 'plane', 'lipstick', 'freezer']
}

# Swap the button in Box 1 with the meteor in Box 4.
boxes[1].remove('button')
boxes[4].remove('meteor')
boxes[1].append('meteor')
boxes[4].append('button')

# Remove the rock from Box 2.
boxes[2].remove('rock')

# Replace the telescope and the meteor with the hat and the jungle in Box 1.
boxes[1].remove('telescope')
boxes[1].remove('meteor')
boxes[1].append('hat')
boxes[1].append('jungle')

# Put the shampoo and the coral and the boat into Box 4.
items_to_add = ['shampoo', 'coral', 'boat']
for item in items_to_add:
    boxes[4].append(item)

# Remove the freezer and the coral and the lipstick from Box 4.
items_to_remove = ['freezer', 'coral', 'lipstick']
for item in items_to_remove:
    boxes[4].remove(item)

# Swap the storm in Box 0 with the button in Box 4.
boxes[0].remove('storm')
boxes[4].remove('button')
boxes[0].append('button')
boxes[4].append('storm')

# Put the controller and the star and the vase into Box 0.
items_to_add = ['controller', 'star', 'vase']
for item in items_to_add:
    boxes[0].append(item)

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")