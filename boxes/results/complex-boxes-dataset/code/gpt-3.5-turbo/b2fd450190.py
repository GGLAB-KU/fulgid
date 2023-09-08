# Initial state of boxes
boxes = {
    0: [],
    1: ['fish', 'cup', 'toy'],
    2: ['telescope', 'dress', 'fork', 'shark'],
    3: [],
    4: ['pot', 'swimsuit', 'razor', 'sun', 'soap']
}

# Swap the toy in Box 1 with the sun in Box 4.
boxes[1].remove('toy')
boxes[4].remove('sun')
boxes[1].append('sun')
boxes[4].append('toy')

# Move the fish from Box 1 to Box 2.
boxes[1].remove('fish')
boxes[2].append('fish')

# Swap the toy in Box 4 with the fish in Box 2.
boxes[4].remove('toy')
boxes[2].remove('fish')
boxes[4].append('fish')
boxes[2].append('toy')

# Move the razor from Box 4 to Box 0.
boxes[4].remove('razor')
boxes[0].append('razor')

# Remove the pot and the soap from Box 4.
boxes[4].remove('pot')
boxes[4].remove('soap')

# Remove the shark from Box 2.
boxes[2].remove('shark')

# Remove the dress and the fork from Box 2.
boxes[2].remove('dress')
boxes[2].remove('fork')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")