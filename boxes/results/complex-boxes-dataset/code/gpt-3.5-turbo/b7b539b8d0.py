# Initial state of boxes
boxes = {
    0: ['guitar'],
    1: ['boot', 'zipper', 'perfume', 'pen', 'helmet'],
    2: ['flute', 'comb', 'pillow', 'dog'],
    3: ['swimsuit', 'needle', 'cow', 'bag'],
    4: ['jungle', 'violin', 'sculpture'],
    5: ['wire'],
    6: ['mixer', 'frame', 'motorcycle', 'mirror'],
    7: ['basket', 'storm', 'bracelet', 'mask', 'pot'],
    8: ['flower', 'shorts', 'toy', 'oven'],
    9: ['ship', 'pants']
}

# Replace the boot and the perfume and the pen with the game and the scarf and the camera in Box 1.
boxes[1].remove('boot')
boxes[1].remove('perfume')
boxes[1].remove('pen')
boxes[1].append('game')
boxes[1].append('scarf')
boxes[1].append('camera')

# Swap the motorcycle in Box 6 with the ship in Box 9.
boxes[6].remove('motorcycle')
boxes[9].remove('ship')
boxes[6].append('ship')
boxes[9].append('motorcycle')

# Remove the frame and the mixer and the mirror from Box 6.
boxes[6].remove('frame')
boxes[6].remove('mixer')
boxes[6].remove('mirror')

# Replace the wire with the tie in Box 5.
boxes[5].remove('wire')
boxes[5].append('tie')

# Move the ship from Box 6 to Box 8.
boxes[6].remove('ship')
boxes[8].append('ship')

# Remove the storm and the mask from Box 7.
boxes[7].remove('storm')
boxes[7].remove('mask')

# Move the violin and the jungle and the sculpture from Box 4 to Box 0.
items_to_move = ['violin', 'jungle', 'sculpture']
for item in items_to_move:
    boxes[4].remove(item)
    boxes[0].append(item)

# Move the motorcycle from Box 9 to Box 4.
boxes[9].remove('motorcycle')
boxes[4].append('motorcycle')

# Move the tie from Box 5 to Box 7.
boxes[5].remove('tie')
boxes[7].append('tie')

# Move the motorcycle from Box 4 to Box 3.
boxes[4].remove('motorcycle')
boxes[3].append('motorcycle')

# Replace the pants with the motorcycle in Box 9.
boxes[9].remove('pants')
boxes[9].append('motorcycle')

# Replace the camera with the leaf in Box 1.
boxes[1].remove('camera')
boxes[1].append('leaf')

# Replace the comb with the ocean in Box 2.
boxes[2].remove('comb')
boxes[2].append('ocean')

# Remove the oven and the flower from Box 8.
boxes[8].remove('oven')
boxes[8].remove('flower')

# Swap the flute in Box 2 with the game in Box 1.
boxes[2].remove('flute')
boxes[1].remove('game')
boxes[2].append('game')
boxes[1].append('flute')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")