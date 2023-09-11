# Initial state of boxes
boxes = {
    0: ['battery', 'fridge'],
    1: ['cup', 'needle'],
    2: ['butterfly'],
    3: ['wire', 'horn', 'clock']
}

# Replace the clock and the horn and the wire with the hat and the dice and the wallet in Box 3.
boxes[3].remove('clock')
boxes[3].remove('horn')
boxes[3].remove('wire')
boxes[3].append('hat')
boxes[3].append('dice')
boxes[3].append('wallet')

# Empty Box 0.
boxes[0] = []

# Move the butterfly from Box 2 to Box 0.
boxes[0].append(boxes[2].pop())

# Put the doll and the storm and the game into Box 3.
boxes[3].append('doll')
boxes[3].append('storm')
boxes[3].append('game')

# Swap the storm in Box 3 with the butterfly in Box 0.
boxes[0].append(boxes[3].pop(boxes[3].index('storm')))
boxes[3].append(boxes[0].pop())

# Put the plane and the fish and the watch into Box 3.
boxes[3].append('plane')
boxes[3].append('fish')
boxes[3].append('watch')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")