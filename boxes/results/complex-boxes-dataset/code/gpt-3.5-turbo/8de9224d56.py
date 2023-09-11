# Initial state of boxes
boxes = {
    0: ['necklace', 'mixer', 'toothpaste', 'microscope', 'rain'],
    1: ['storm', 'sun', 'shorts'],
    2: ['piano'],
    3: ['telescope', 'jacket'],
    4: ['glove', 'bell'],
    5: ['belt', 'wire', 'apple'],
    6: []
}

# Replace the piano with the book in Box 2.
boxes[2].remove('piano')
boxes[2].append('book')

# Move the glove and the bell from Box 4 to Box 6.
boxes[4].remove('glove')
boxes[4].remove('bell')
boxes[6].append('glove')
boxes[6].append('bell')

# Move the mixer from Box 0 to Box 1.
boxes[0].remove('mixer')
boxes[1].append('mixer')

# Remove the apple and the wire and the belt from Box 5.
items_to_remove = ['apple', 'wire', 'belt']
for item in items_to_remove:
    boxes[5].remove(item)

# Put the book into Box 0.
boxes[0].append('book')

# Move the telescope and the jacket from Box 3 to Box 6.
boxes[3].remove('telescope')
boxes[3].remove('jacket')
boxes[6].append('telescope')
boxes[6].append('jacket')

# Remove the book from Box 2.
boxes[2].remove('book')

# Replace the toothpaste with the comb in Box 0.
boxes[0].remove('toothpaste')
boxes[0].append('comb')

# Swap the storm in Box 1 with the bell in Box 6.
boxes[1].remove('storm')
boxes[6].remove('bell')
boxes[1].append('bell')
boxes[6].append('storm')

# Swap the storm in Box 6 with the rain in Box 0.
boxes[0].remove('rain')
boxes[6].remove('storm')
boxes[0].append('storm')
boxes[6].append('rain')

# Replace the sun and the bell with the motorcycle and the plane in Box 1.
boxes[1].remove('sun')
boxes[1].remove('bell')
boxes[1].append('motorcycle')
boxes[1].append('plane')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")