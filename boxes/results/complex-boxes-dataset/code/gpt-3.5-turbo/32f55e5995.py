# Initial state of boxes
boxes = {
    0: ['cat', 'basket', 'comb', 'submarine'],
    1: ['horse', 'toaster', 'shampoo', 'bowl', 'lock'],
    2: ['mask', 'crown'],
    3: [],
    4: ['laptop', 'violin', 'coral'],
    5: ['umbrella', 'butterfly'],
    6: ['tiger', 'jungle']
}

# Replace the tiger with the fridge in Box 6.
boxes[6].remove('tiger')
boxes[6].append('fridge')

# Move the fridge and the jungle from Box 6 to Box 5.
items_to_move = ['fridge', 'jungle']
for item in items_to_move:
    boxes[6].remove(item)
    boxes[5].append(item)

# Put the whistle and the fork into Box 4.
items_to_put = ['whistle', 'fork']
for item in items_to_put:
    boxes[4].append(item)

# Move the lock and the toaster from Box 1 to Box 6.
items_to_move = ['lock', 'toaster']
for item in items_to_move:
    boxes[1].remove(item)
    boxes[6].append(item)

# Remove the whistle and the laptop from Box 4.
items_to_remove = ['whistle', 'laptop']
for item in items_to_remove:
    boxes[4].remove(item)

# Remove the toaster from Box 6.
boxes[6].remove('toaster')

# Swap the butterfly in Box 5 with the horse in Box 1.
boxes[5].remove('butterfly')
boxes[1].remove('horse')
boxes[5].append('horse')
boxes[1].append('butterfly')

# Empty Box 6.
boxes[6] = []

# Move the horse and the umbrella from Box 5 to Box 4.
items_to_move = ['horse', 'umbrella']
for item in items_to_move:
    boxes[5].remove(item)
    boxes[4].append(item)

# Put the shark and the flower and the pan into Box 6.
items_to_put = ['shark', 'flower', 'pan']
for item in items_to_put:
    boxes[6].append(item)

# Remove the shampoo from Box 1.
boxes[1].remove('shampoo')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")