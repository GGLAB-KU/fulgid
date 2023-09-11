# Initial state of boxes
boxes = {
    0: ['grinder', 'pillow', 'whistle', 'zipper', 'forest'],
    1: ['pot'],
    2: [],
    3: ['leaf'],
    4: ['controller', 'puzzle'],
    5: ['flute', 'coral', 'pan', 'microscope', 'game'],
    6: []
}

# Move the leaf from Box 3 to Box 4.
boxes[3].remove('leaf')
boxes[4].append('leaf')

# Put the jacket into Box 3.
boxes[3].append('jacket')

# Replace the jacket with the guitar in Box 3.
boxes[3].remove('jacket')
boxes[3].append('guitar')

# Replace the guitar with the cow in Box 3.
boxes[3].remove('guitar')
boxes[3].append('cow')

# Put the comb into Box 3.
boxes[3].append('comb')

# Swap the cow in Box 3 with the pot in Box 1.
boxes[3].remove('cow')
boxes[1].remove('pot')
boxes[3].append('pot')
boxes[1].append('cow')

# Swap the comb in Box 3 with the cow in Box 1.
boxes[3].remove('comb')
boxes[1].remove('cow')
boxes[3].append('cow')
boxes[1].append('comb')

# Put the swimsuit into Box 6.
boxes[6].append('swimsuit')

# Swap the cow in Box 3 with the controller in Box 4.
boxes[3].remove('cow')
boxes[4].remove('controller')
boxes[3].append('controller')
boxes[4].append('cow')

# Move the pot from Box 3 to Box 2.
boxes[3].remove('pot')
boxes[2].append('pot')

# Swap the pot in Box 2 with the pan in Box 5.
boxes[2].remove('pot')
boxes[5].remove('pan')
boxes[2].append('pan')
boxes[5].append('pot')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")