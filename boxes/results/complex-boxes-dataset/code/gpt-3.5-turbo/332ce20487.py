# Initial state of boxes
boxes = {
    0: ['submarine'],
    1: ['bird', 'brush', 'wig', 'skirt', 'river'],
    2: ['harmonica'],
    3: ['sandals', 'candle'],
    4: ['ship', 'planet', 'shirt', 'dice', 'coral']
}

# Put the earring and the dice into Box 1.
boxes[1].append('earring')
boxes[1].append('dice')

# Remove the brush from Box 1.
boxes[1].remove('brush')

# Remove the planet and the dice and the shirt from Box 4.
items_to_remove = ['planet', 'dice', 'shirt']
for item in items_to_remove:
    boxes[4].remove(item)

# Replace the sandals with the pen in Box 3.
boxes[3].remove('sandals')
boxes[3].append('pen')

# Put the grinder and the book and the ring into Box 1.
items_to_put = ['grinder', 'book', 'ring']
for item in items_to_put:
    boxes[1].append(item)

# Swap the wig in Box 1 with the pen in Box 3.
boxes[1].remove('wig')
boxes[3].remove('pen')
boxes[1].append('pen')
boxes[3].append('wig')

# Move the harmonica from Box 2 to Box 4.
boxes[2].remove('harmonica')
boxes[4].append('harmonica')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")