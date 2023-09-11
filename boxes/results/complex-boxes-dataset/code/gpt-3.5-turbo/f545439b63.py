# Initial state of boxes
boxes = {
    0: ['toothpaste', 'vase', 'moon', 'grass', 'helmet'],
    1: [],
    2: ['makeup', 'skirt'],
    3: ['thunder', 'wallet', 'snow', 'violin'],
    4: []
}

# Move the helmet and the grass from Box 0 to Box 4.
boxes[0].remove('helmet')
boxes[0].remove('grass')
boxes[4].append('helmet')
boxes[4].append('grass')

# Empty Box 0.
boxes[0] = []

# Put the guitar and the leaf and the gloves into Box 0.
boxes[0].append('guitar')
boxes[0].append('leaf')
boxes[0].append('gloves')

# Swap the makeup in Box 2 with the grass in Box 4.
boxes[2].remove('makeup')
boxes[4].remove('grass')
boxes[2].append('grass')
boxes[4].append('makeup')

# Replace the violin with the drum in Box 3.
boxes[3].remove('violin')
boxes[3].append('drum')

# Put the makeup into Box 3.
boxes[3].append('makeup')

# Move the leaf from Box 0 to Box 4.
boxes[0].remove('leaf')
boxes[4].append('leaf')

# Remove the wallet and the drum from Box 3.
boxes[3].remove('wallet')
boxes[3].remove('drum')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")