# Initial state of boxes
boxes = {
    0: ['zipper', 'rock'],
    1: [],
    2: ['button', 'clock', 'spoon'],
    3: ['horn', 'key', 'jacket'],
    4: ['starfish', 'basket', 'island'],
    5: ['tie'],
    6: ['game', 'gloves', 'paint', 'tree']
}

# Put the star into Box 1.
boxes[1].append('star')

# Remove the rock and the zipper from Box 0.
boxes[0].remove('rock')
boxes[0].remove('zipper')

# Put the dress into Box 2.
boxes[2].append('dress')

# Put the meteor and the coral into Box 2.
boxes[2].append('meteor')
boxes[2].append('coral')

# Move the basket from Box 4 to Box 6.
boxes[4].remove('basket')
boxes[6].append('basket')

# Swap the starfish in Box 4 with the gloves in Box 6.
boxes[4].remove('starfish')
boxes[6].remove('gloves')
boxes[4].append('gloves')
boxes[6].append('starfish')

# Move the tie from Box 5 to Box 2.
boxes[5].remove('tie')
boxes[2].append('tie')

# Remove the coral from Box 2.
boxes[2].remove('coral')

# Remove the meteor and the spoon from Box 2.
boxes[2].remove('meteor')
boxes[2].remove('spoon')

# Remove the starfish from Box 6.
boxes[6].remove('starfish')

# Swap the star in Box 1 with the jacket in Box 3.
boxes[1].remove('star')
boxes[3].remove('jacket')
boxes[1].append('jacket')
boxes[3].append('star')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")