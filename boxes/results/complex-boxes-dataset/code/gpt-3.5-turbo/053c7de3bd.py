# Initial state of boxes
boxes = {
    0: ['river'],
    1: [],
    2: ['fridge', 'basket', 'button'],
    3: ['tree', 'butterfly']
}

# Move the fridge and the button from Box 2 to Box 1.
boxes[2].remove('fridge')
boxes[2].remove('button')
boxes[1].append('fridge')
boxes[1].append('button')

# Remove the basket from Box 2.
boxes[2].remove('basket')

# Move the fridge from Box 1 to Box 0.
boxes[1].remove('fridge')
boxes[0].append('fridge')

# Replace the butterfly and the tree with the pan and the snow in Box 3.
boxes[3].remove('butterfly')
boxes[3].remove('tree')
boxes[3].append('pan')
boxes[3].append('snow')

# Put the lion and the cup into Box 3.
boxes[3].append('lion')
boxes[3].append('cup')

# Put the controller and the plate and the comb into Box 0.
boxes[0].append('controller')
boxes[0].append('plate')
boxes[0].append('comb')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")