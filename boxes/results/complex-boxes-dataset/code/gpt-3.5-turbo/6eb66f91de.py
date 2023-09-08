# Initial state of boxes
boxes = {
    0: ['polish', 'mixer'],
    1: ['comb', 'laptop', 'submarine', 'shoes', 'perfume'],
    2: ['jungle', 'shark', 'note', 'telescope'],
    3: ['shampoo'],
    4: ['book'],
    5: []
}

# Move the polish from Box 0 to Box 5.
boxes[0].remove('polish')
boxes[5].append('polish')

# Empty Box 1.
boxes[1] = []

# Move the mixer from Box 0 to Box 3.
boxes[0].remove('mixer')
boxes[3].append('mixer')

# Put the cow and the glove and the comet into Box 4.
items_to_move = ['cow', 'glove', 'comet']
for item in items_to_move:
    boxes[4].append(item)

# Move the jungle from Box 2 to Box 1.
boxes[2].remove('jungle')
boxes[1].append('jungle')

# Swap the jungle in Box 1 with the mixer in Box 3.
boxes[1].remove('jungle')
boxes[3].remove('mixer')
boxes[1].append('mixer')
boxes[3].append('jungle')

# Swap the mixer in Box 1 with the note in Box 2.
boxes[1].remove('mixer')
boxes[2].remove('note')
boxes[1].append('note')
boxes[2].append('mixer')

# Replace the polish with the pen in Box 5.
boxes[5].remove('polish')
boxes[5].append('pen')

# Move the glove from Box 4 to Box 1.
boxes[4].remove('glove')
boxes[1].append('glove')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")