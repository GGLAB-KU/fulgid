# Initial state of boxes
boxes = {
    0: ['tree'],
    1: ['battery', 'candle', 'cloud'],
    2: ['card', 'pillow', 'blender', 'charger', 'pants'],
    3: ['mask', 'soap', 'dog'],
    4: ['thread', 'snow'],
    5: ['puzzle', 'vase'],
    6: ['boot'],
    7: ['bus', 'usb'],
    8: ['flute', 'glasses', 'spoon'],
    9: [],
    10: [],
    11: ['bag', 'brush', 'wallet', 'microscope', 'seaweed'],
    12: ['ocean']
}

# Swap the battery in Box 1 with the ocean in Box 12.
boxes[1].remove('battery')
boxes[12].remove('ocean')
boxes[1].append('ocean')
boxes[12].append('battery')

# Remove the vase from Box 5.
boxes[5].remove('vase')

# Remove the blender from Box 2.
boxes[2].remove('blender')

# Remove the puzzle from Box 5.
boxes[5].remove('puzzle')

# Replace the soap with the key in Box 3.
boxes[3].remove('soap')
boxes[3].append('key')

# Move the usb and the bus from Box 7 to Box 1.
items_to_move = ['usb', 'bus']
for item in items_to_move:
    boxes[7].remove(item)
    boxes[1].append(item)

# Move the pillow from Box 2 to Box 12.
boxes[2].remove('pillow')
boxes[12].append('pillow')

# Replace the thread with the toothbrush in Box 4.
boxes[4].remove('thread')
boxes[4].append('toothbrush')

# Swap the pillow in Box 12 with the seaweed in Box 11.
boxes[12].remove('pillow')
boxes[11].remove('seaweed')
boxes[12].append('seaweed')
boxes[11].append('pillow')

# Swap the pillow in Box 11 with the snow in Box 4.
boxes[11].remove('pillow')
boxes[4].remove('snow')
boxes[11].append('snow')
boxes[4].append('pillow')

# Swap the tree in Box 0 with the mask in Box 3.
boxes[0].remove('tree')
boxes[3].remove('mask')
boxes[0].append('mask')
boxes[3].append('tree')

# Swap the mask in Box 0 with the pillow in Box 4.
boxes[0].remove('mask')
boxes[4].remove('pillow')
boxes[0].append('pillow')
boxes[4].append('mask')

# Put the vase into Box 6.
boxes[6].append('vase')

# Put the moon into Box 12.
boxes[12].append('moon')

# Remove the toothbrush from Box 4.
boxes[4].remove('toothbrush')

# Remove the cloud from Box 1.
boxes[1].remove('cloud')

# Swap the vase in Box 6 with the key in Box 3.
boxes[6].remove('vase')
boxes[3].remove('key')
boxes[6].append('key')
boxes[3].append('vase')

# Remove the candle and the bus from Box 1.
boxes[1].remove('candle')
boxes[1].remove('bus')

# Put the cat and the tape into Box 10.
boxes[10].extend(['cat', 'tape'])

# Replace the spoon and the flute with the planet and the basket in Box 8.
boxes[8].remove('spoon')
boxes[8].remove('flute')
boxes[8].append('planet')
boxes[8].append('basket')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")