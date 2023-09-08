# Initial state of boxes
boxes = {
    0: [],
    1: ['shirt', 'truck', 'skirt', 'toaster', 'oven'],
    2: [],
    3: ['flower'],
    4: ['planet', 'magnet', 'flute', 'bell', 'wire'],
    5: [],
    6: ['hat', 'guitar', 'lamp', 'fish', 'cat'],
    7: [],
    8: ['mountain', 'rain', 'butterfly'],
    9: ['grass'],
    10: ['bird', 'sun', 'pot', 'mask'],
    11: ['drum'],
    12: ['mixer'],
    13: ['coat'],
    14: []
}

# Move the bell and the flute from Box 4 to Box 9.
boxes[4].remove('bell')
boxes[4].remove('flute')
boxes[9].append('bell')
boxes[9].append('flute')

# Put the table into Box 14.
boxes[14].append('table')

# Swap the grass in Box 9 with the butterfly in Box 8.
boxes[9].remove('grass')
boxes[8].remove('butterfly')
boxes[9].append('butterfly')
boxes[8].append('grass')

# Replace the coat with the pot in Box 13.
boxes[13].remove('coat')
boxes[13].append('pot')

# Remove the oven and the skirt from Box 1.
boxes[1].remove('oven')
boxes[1].remove('skirt')

# Move the flower from Box 3 to Box 5.
boxes[3].remove('flower')
boxes[5].append('flower')

# Empty Box 14.
boxes[14] = []

# Put the battery and the harmonica into Box 4.
boxes[4].append('battery')
boxes[4].append('harmonica')

# Move the mixer from Box 12 to Box 9.
boxes[12].remove('mixer')
boxes[9].append('mixer')

# Put the submarine into Box 5.
boxes[5].append('submarine')

# Replace the pot with the storm in Box 10.
boxes[10].remove('pot')
boxes[10].append('storm')

# Replace the butterfly and the mixer and the flute with the island and the bus and the mask in Box 9.
boxes[9].remove('butterfly')
boxes[9].remove('mixer')
boxes[9].remove('flute')
boxes[9].append('island')
boxes[9].append('bus')
boxes[9].append('mask')

# Replace the truck with the blender in Box 1.
boxes[1].remove('truck')
boxes[1].append('blender')

# Move the fish and the lamp from Box 6 to Box 2.
boxes[6].remove('fish')
boxes[6].remove('lamp')
boxes[2].append('fish')
boxes[2].append('lamp')

# Put the camera and the lightning and the mask into Box 0.
boxes[0].append('camera')
boxes[0].append('lightning')
boxes[0].append('mask')

# Replace the storm and the sun and the mask with the brush and the harmonica and the coral in Box 10.
boxes[10].remove('storm')
boxes[10].remove('sun')
boxes[10].remove('mask')
boxes[10].append('brush')
boxes[10].append('harmonica')
boxes[10].append('coral')

# Move the brush and the coral and the bird from Box 10 to Box 0.
boxes[10].remove('brush')
boxes[10].remove('coral')
boxes[10].remove('bird')
boxes[0].append('brush')
boxes[0].append('coral')
boxes[0].append('bird')

# Empty Box 9.
boxes[9] = []

# Swap the lamp in Box 2 with the toaster in Box 1.
boxes[2].remove('lamp')
boxes[1].remove('toaster')
boxes[2].append('toaster')
boxes[1].append('lamp')

# Replace the grass with the fork in Box 8.
boxes[8].remove('grass')
boxes[8].append('fork')

# Move the harmonica from Box 10 to Box 7.
boxes[10].remove('harmonica')
boxes[7].append('harmonica')

# Move the flower and the submarine from Box 5 to Box 11.
boxes[5].remove('flower')
boxes[5].remove('submarine')
boxes[11].append('flower')
boxes[11].append('submarine')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")