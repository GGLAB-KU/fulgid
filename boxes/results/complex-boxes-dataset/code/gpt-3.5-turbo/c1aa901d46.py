# Initial state of boxes
boxes = {
    0: ['oven'],
    1: [],
    2: ['fridge'],
    3: []
}

# Replace the oven with the candle in Box 0.
boxes[0].remove('oven')
boxes[0].append('candle')

# Swap the fridge in Box 2 with the candle in Box 0.
boxes[0].remove('candle')
boxes[2].remove('fridge')
boxes[0].append('fridge')
boxes[2].append('candle')

# Put the butterfly and the bag into Box 0.
boxes[0].append('butterfly')
boxes[0].append('bag')

# Replace the candle with the skirt in Box 2.
boxes[2].remove('candle')
boxes[2].append('skirt')

# Move the skirt from Box 2 to Box 0.
boxes[2].remove('skirt')
boxes[0].append('skirt')

# Move the fridge and the skirt from Box 0 to Box 2.
boxes[0].remove('fridge')
boxes[0].remove('skirt')
boxes[2].append('fridge')
boxes[2].append('skirt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")