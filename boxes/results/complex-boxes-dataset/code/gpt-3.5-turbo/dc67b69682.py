# Initial state of boxes
boxes = {
    0: [],
    1: ['candle'],
    2: ['glasses', 'speaker'],
    3: ['cloud', 'coral', 'glove', 'jacket', 'dog']
}

# Swap the candle in Box 1 with the dog in Box 3.
boxes[1].remove('candle')
boxes[3].remove('dog')
boxes[1].append('dog')
boxes[3].append('candle')

# Move the dog from Box 1 to Box 0.
boxes[1].remove('dog')
boxes[0].append('dog')

# Replace the speaker and the glasses with the coin and the flute in Box 2.
boxes[2].remove('speaker')
boxes[2].remove('glasses')
boxes[2].append('coin')
boxes[2].append('flute')

# Move the dog from Box 0 to Box 3.
boxes[0].remove('dog')
boxes[3].append('dog')

# Put the grass into Box 1.
boxes[1].append('grass')

# Swap the grass in Box 1 with the flute in Box 2.
boxes[1].remove('grass')
boxes[2].remove('flute')
boxes[1].append('flute')
boxes[2].append('grass')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")