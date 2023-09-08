# Initial state of boxes
boxes = {
    0: ['coat', 'candle'],
    1: ['oven'],
    2: [],
    3: ['meteor', 'jungle'],
    4: ['lion', 'necklace']
}

# Swap the candle in Box 0 with the meteor in Box 3.
boxes[0].remove('candle')
boxes[3].remove('meteor')
boxes[0].append('meteor')
boxes[3].append('candle')

# Remove the meteor from Box 0.
boxes[0].remove('meteor')

# Replace the candle with the note in Box 3.
boxes[3].remove('candle')
boxes[3].append('note')

# Put the apple and the mirror into Box 3.
boxes[3].append('apple')
boxes[3].append('mirror')

# Put the sculpture into Box 1.
boxes[1].append('sculpture')

# Move the oven from Box 1 to Box 2.
boxes[1].remove('oven')
boxes[2].append('oven')

# Move the jungle and the apple from Box 3 to Box 4.
boxes[3].remove('jungle')
boxes[3].remove('apple')
boxes[4].append('jungle')
boxes[4].append('apple')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")