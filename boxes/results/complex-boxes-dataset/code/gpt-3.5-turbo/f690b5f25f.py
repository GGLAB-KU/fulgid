# Initial state of boxes
boxes = {
    0: ['bag', 'helmet', 'laptop'],
    1: ['pot', 'blender'],
    2: ['button', 'pan', 'motorcycle'],
    3: ['candle', 'card', 'umbrella'],
    4: ['watch', 'dolphin', 'shampoo', 'microscope', 'speaker'],
    5: ['sandals', 'planet', 'thunder']
}

# Empty Box 5
boxes[5] = []

# Move the button from Box 2 to Box 5
boxes[2].remove('button')
boxes[5].append('button')

# Replace the umbrella with the earring in Box 3
boxes[3].remove('umbrella')
boxes[3].append('earring')

# Replace the card with the needle in Box 3
boxes[3].remove('card')
boxes[3].append('needle')

# Swap the motorcycle in Box 2 with the blender in Box 1
boxes[2].remove('motorcycle')
boxes[1].remove('blender')
boxes[2].append('blender')
boxes[1].append('motorcycle')

# Replace the pot with the tree in Box 1
boxes[1].remove('pot')
boxes[1].append('tree')

# Replace the helmet and the bag and the laptop with the bird and the shark and the shirt in Box 0
boxes[0].remove('helmet')
boxes[0].remove('bag')
boxes[0].remove('laptop')
boxes[0].append('bird')
boxes[0].append('shark')
boxes[0].append('shirt')

# Empty Box 1
boxes[1] = []

# Remove the button from Box 5
boxes[5].remove('button')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")