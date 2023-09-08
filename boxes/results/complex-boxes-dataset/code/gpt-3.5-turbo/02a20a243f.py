# Initial state of boxes
boxes = {
    0: ['battery'],
    1: [],
    2: ['telescope'],
    3: ['spoon'],
    4: ['laptop'],
    5: ['shelf'],
    6: ['elephant', 'soap'],
    7: [],
    8: ['ring', 'coin', 'mixer'],
    9: [],
    10: [],
    11: ['note'],
    12: ['bowl', 'usb', 'moon', 'bag', 'bear'],
    13: ['candle', 'dice', 'cow']
}

# Remove the candle and the cow and the dice from Box 13.
boxes[13].remove('candle')
boxes[13].remove('dice')
boxes[13].remove('cow')

# Put the towel and the tree into Box 13.
boxes[13].append('towel')
boxes[13].append('tree')

# Move the bag and the usb from Box 12 to Box 11.
boxes[12].remove('bag')
boxes[12].remove('usb')
boxes[11].append('bag')
boxes[11].append('usb')

# Move the bear from Box 12 to Box 10.
boxes[12].remove('bear')
boxes[10].append('bear')

# Move the soap and the elephant from Box 6 to Box 11.
boxes[6].remove('soap')
boxes[6].remove('elephant')
boxes[11].append('soap')
boxes[11].append('elephant')

# Move the spoon from Box 3 to Box 0.
boxes[3].remove('spoon')
boxes[0].append('spoon')

# Put the console and the plane and the pot into Box 3.
boxes[3].append('console')
boxes[3].append('plane')
boxes[3].append('pot')

# Empty Box 13.
boxes[13] = []

# Put the microwave into Box 11.
boxes[11].append('microwave')

# Remove the bear from Box 10.
boxes[10].remove('bear')

# Remove the mixer and the ring from Box 8.
boxes[8].remove('mixer')
boxes[8].remove('ring')

# Replace the spoon and the battery with the puzzle and the mirror in Box 0.
boxes[0].remove('spoon')
boxes[0].remove('battery')
boxes[0].append('puzzle')
boxes[0].append('mirror')

# Put the brush and the flute and the pot into Box 13.
boxes[13].append('brush')
boxes[13].append('flute')
boxes[13].append('pot')

# Replace the brush with the lipstick in Box 13.
boxes[13].remove('brush')
boxes[13].append('lipstick')

# Swap the moon in Box 12 with the puzzle in Box 0.
boxes[12].remove('moon')
boxes[0].remove('puzzle')
boxes[12].append('puzzle')
boxes[0].append('moon')

# Move the shelf from Box 5 to Box 4.
boxes[5].remove('shelf')
boxes[4].append('shelf')

# Swap the moon in Box 0 with the coin in Box 8.
boxes[0].remove('moon')
boxes[8].remove('coin')
boxes[0].append('coin')
boxes[8].append('moon')

# Remove the laptop and the shelf from Box 4.
boxes[4].remove('laptop')
boxes[4].remove('shelf')

# Swap the flute in Box 13 with the moon in Box 8.
boxes[13].remove('flute')
boxes[8].remove('moon')
boxes[13].append('moon')
boxes[8].append('flute')

# Move the puzzle from Box 12 to Box 4.
boxes[12].remove('puzzle')
boxes[4].append('puzzle')

# Move the flute from Box 8 to Box 7.
boxes[8].remove('flute')
boxes[7].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")