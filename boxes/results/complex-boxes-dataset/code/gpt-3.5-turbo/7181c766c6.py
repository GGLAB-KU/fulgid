# Initial state of boxes
boxes = {
    0: ['magnet', 'tiger', 'basket'],
    1: ['table'],
    2: ['thunder'],
    3: [],
    4: [],
    5: ['shoes', 'shelf', 'cat']
}

# Remove the basket from Box 0.
boxes[0].remove('basket')

# Replace the tiger and the magnet with the snow and the motorcycle in Box 0.
boxes[0].remove('tiger')
boxes[0].remove('magnet')
boxes[0].append('snow')
boxes[0].append('motorcycle')

# Swap the table in Box 1 with the shelf in Box 5.
boxes[1].remove('table')
boxes[5].remove('shelf')
boxes[1].append('shelf')
boxes[5].append('table')

# Move the snow and the motorcycle from Box 0 to Box 2.
boxes[0].remove('snow')
boxes[0].remove('motorcycle')
boxes[2].append('snow')
boxes[2].append('motorcycle')

# Replace the shoes and the table and the cat with the note and the necklace and the grass in Box 5.
boxes[5].remove('shoes')
boxes[5].remove('table')
boxes[5].remove('cat')
boxes[5].append('note')
boxes[5].append('necklace')
boxes[5].append('grass')

# Remove the thunder and the snow and the motorcycle from Box 2.
boxes[2].remove('thunder')
boxes[2].remove('snow')
boxes[2].remove('motorcycle')

# Replace the shelf with the makeup in Box 1.
boxes[1].remove('shelf')
boxes[1].append('makeup')

# Replace the makeup with the elephant in Box 1.
boxes[1].remove('makeup')
boxes[1].append('elephant')

# Replace the note and the necklace with the shampoo and the ring in Box 5.
boxes[5].remove('note')
boxes[5].remove('necklace')
boxes[5].append('shampoo')
boxes[5].append('ring')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")