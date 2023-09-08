# Initial state of boxes
boxes = {
    0: ['paint', 'sandals'],
    1: [],
    2: ['makeup', 'lightning', 'cloud', 'cup'],
    3: ['candle', 'horn', 'magnet', 'wire'],
    4: ['note', 'desert', 'fridge', 'gloves', 'sock'],
    5: ['plate', 'island', 'ring', 'forest'],
    6: [],
    7: ['toy', 'storm', 'pillow', 'shoes'],
    8: ['boot', 'toaster', 'bird'],
    9: ['spoon'],
    10: ['mask', 'fish']
}

# Replace the note and the desert and the gloves with the car and the makeup and the river in Box 4.
boxes[4].remove('note')
boxes[4].remove('desert')
boxes[4].remove('gloves')
boxes[4].append('car')
boxes[4].append('makeup')
boxes[4].append('river')

# Replace the paint and the sandals with the frame and the mixer in Box 0.
boxes[0].remove('paint')
boxes[0].remove('sandals')
boxes[0].append('frame')
boxes[0].append('mixer')

# Empty Box 4.
boxes[4] = []

# Replace the magnet with the microscope in Box 3.
boxes[3].remove('magnet')
boxes[3].append('microscope')

# Replace the frame and the mixer with the jacket and the storm in Box 0.
boxes[0].remove('frame')
boxes[0].remove('mixer')
boxes[0].append('jacket')
boxes[0].append('storm')

# Replace the jacket and the storm with the thread and the apple in Box 0.
boxes[0].remove('jacket')
boxes[0].remove('storm')
boxes[0].append('thread')
boxes[0].append('apple')

# Empty Box 0.
boxes[0] = []

# Put the wallet into Box 8.
boxes[8].append('wallet')

# Remove the spoon from Box 9.
boxes[9].remove('spoon')

# Swap the pillow in Box 7 with the ring in Box 5.
boxes[7].remove('pillow')
boxes[5].remove('ring')
boxes[7].append('ring')
boxes[5].append('pillow')

# Put the dice into Box 10.
boxes[10].append('dice')

# Swap the wire in Box 3 with the makeup in Box 2.
boxes[3].remove('wire')
boxes[2].remove('makeup')
boxes[3].append('makeup')
boxes[2].append('wire')

# Swap the dice in Box 10 with the plate in Box 5.
boxes[10].remove('dice')
boxes[5].remove('plate')
boxes[10].append('plate')
boxes[5].append('dice')

# Remove the horn and the candle from Box 3.
boxes[3].remove('horn')
boxes[3].remove('candle')

# Move the fish and the mask from Box 10 to Box 6.
boxes[10].remove('fish')
boxes[10].remove('mask')
boxes[6].append('fish')
boxes[6].append('mask')

# Put the controller and the card into Box 9.
boxes[9].append('controller')
boxes[9].append('card')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")