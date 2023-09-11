# Initial state of boxes
boxes = {
    0: ['book', 'skirt', 'cow'],
    1: [],
    2: ['coin', 'horse'],
    3: ['dress', 'helmet'],
    4: ['frame', 'mixer', 'earring']
}

# Put the shelf and the cat into Box 1.
boxes[1].append('shelf')
boxes[1].append('cat')

# Remove the coin and the horse from Box 2.
boxes[2].remove('coin')
boxes[2].remove('horse')

# Replace the frame with the flower in Box 4.
boxes[4].remove('frame')
boxes[4].append('flower')

# Swap the book in Box 0 with the cat in Box 1.
boxes[0].remove('book')
boxes[1].remove('cat')
boxes[0].append('cat')
boxes[1].append('book')

# Replace the book and the shelf with the tree and the branch in Box 1.
boxes[1].remove('book')
boxes[1].remove('shelf')
boxes[1].append('tree')
boxes[1].append('branch')

# Swap the earring in Box 4 with the cow in Box 0.
boxes[4].remove('earring')
boxes[0].remove('cow')
boxes[4].append('cow')
boxes[0].append('earring')

# Replace the branch and the tree with the bear and the flute in Box 1.
boxes[1].remove('branch')
boxes[1].remove('tree')
boxes[1].append('bear')
boxes[1].append('flute')

# Move the skirt from Box 0 to Box 2.
boxes[0].remove('skirt')
boxes[2].append('skirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")