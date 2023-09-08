# Initial state of boxes
boxes = {
    0: ['ocean', 'harmonica'],
    1: ['note'],
    2: ['desert'],
    3: [],
    4: ['planet', 'flower', 'shorts', 'horse'],
    5: ['polish', 'fish', 'motorcycle'],
    6: ['crown', 'thunder', 'tree', 'blanket', 'bag']
}

# Remove the desert from Box 2.
boxes[2].remove('desert')

# Swap the fish in Box 5 with the note in Box 1.
boxes[1].remove('note')
boxes[5].remove('fish')
boxes[1].append('fish')
boxes[5].append('note')

# Move the fish from Box 1 to Box 3.
boxes[1].remove('fish')
boxes[3].append('fish')

# Replace the fish with the pan in Box 3.
boxes[3].remove('fish')
boxes[3].append('pan')

# Remove the crown and the tree from Box 6.
boxes[6].remove('crown')
boxes[6].remove('tree')

# Remove the harmonica and the ocean from Box 0.
boxes[0].remove('harmonica')
boxes[0].remove('ocean')

# Empty Box 4.
boxes[4] = []

# Put the hat into Box 0.
boxes[0].append('hat')

# Swap the note in Box 5 with the bag in Box 6.
boxes[5].remove('note')
boxes[6].remove('bag')
boxes[5].append('bag')
boxes[6].append('note')

# Swap the polish in Box 5 with the hat in Box 0.
boxes[5].remove('polish')
boxes[0].remove('hat')
boxes[5].append('hat')
boxes[0].append('polish')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")