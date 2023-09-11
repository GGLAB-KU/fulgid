# Initial state of boxes
boxes = {
    0: ['river', 'bag', 'watch', 'cow'],
    1: ['coat', 'pen', 'train', 'lightning'],
    2: [],
    3: ['glasses', 'rocket', 'plane', 'makeup', 'wallet'],
    4: []
}

# Swap the wallet in Box 3 with the coat in Box 1.
boxes[1].remove('coat')
boxes[3].remove('wallet')
boxes[1].append('wallet')
boxes[3].append('coat')

# Move the makeup and the glasses from Box 3 to Box 4.
items_to_move = ['makeup', 'glasses']
for item in items_to_move:
    boxes[3].remove(item)
    boxes[4].append(item)

# Remove the bag from Box 0.
boxes[0].remove('bag')

# Move the river and the watch and the cow from Box 0 to Box 4.
items_to_move = ['river', 'watch', 'cow']
for item in items_to_move:
    boxes[0].remove(item)
    boxes[4].append(item)

# Replace the rocket and the plane with the toaster and the toy in Box 3.
boxes[3].remove('rocket')
boxes[3].remove('plane')
boxes[3].append('toaster')
boxes[3].append('toy')

# Move the cow and the makeup from Box 4 to Box 3.
items_to_move = ['cow', 'makeup']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[3].append(item)

# Remove the train and the pen from Box 1.
items_to_remove = ['train', 'pen']
for item in items_to_remove:
    boxes[1].remove(item)

# Swap the river in Box 4 with the makeup in Box 3.
boxes[4].remove('river')
boxes[3].remove('makeup')
boxes[4].append('makeup')
boxes[3].append('river')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")