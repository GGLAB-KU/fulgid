# Initial state of boxes
boxes = {
    0: ['card', 'desert'],
    1: ['spoon', 'shorts', 'candle'],
    2: ['cow', 'bag', 'tie'],
    3: [],
    4: ['key']
}

# Put the train into Box 4.
boxes[4].append('train')

# Remove the shorts and the candle from Box 1.
boxes[1].remove('shorts')
boxes[1].remove('candle')

# Replace the spoon with the sculpture in Box 1.
boxes[1].remove('spoon')
boxes[1].append('sculpture')

# Replace the train with the truck in Box 4.
boxes[4].remove('train')
boxes[4].append('truck')

# Swap the desert in Box 0 with the cow in Box 2.
boxes[0].remove('desert')
boxes[2].remove('cow')
boxes[0].append('cow')
boxes[2].append('desert')

# Swap the key in Box 4 with the card in Box 0.
boxes[4].remove('key')
boxes[0].remove('card')
boxes[4].append('card')
boxes[0].append('key')

# Replace the key and the cow with the oven and the boat in Box 0.
boxes[0].remove('key')
boxes[2].remove('cow')
boxes[0].append('oven')
boxes[2].append('boat')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")