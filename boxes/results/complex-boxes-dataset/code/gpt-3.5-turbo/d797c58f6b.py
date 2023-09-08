# Initial state of boxes
boxes = {
    0: ['island'],
    1: ['plane', 'controller', 'wig', 'puzzle'],
    2: ['sock'],
    3: ['elephant', 'pen', 'ship', 'tree', 'flower'],
    4: [],
    5: ['drum', 'bicycle', 'piano', 'belt'],
    6: [],
    7: ['cloud'],
    8: [],
    9: ['table'],
    10: ['star', 'spoon', 'fork'],
    11: []
}

# Replace the cloud with the toothbrush in Box 7.
boxes[7].remove('cloud')
boxes[7].append('toothbrush')

# Move the table from Box 9 to Box 7.
boxes[9].remove('table')
boxes[7].append('table')

# Move the sock from Box 2 to Box 9.
boxes[2].remove('sock')
boxes[9].append('sock')

# Move the island from Box 0 to Box 9.
boxes[0].remove('island')
boxes[9].append('island')

# Replace the island and the sock with the battery and the vase in Box 9.
boxes[9].remove('island')
boxes[9].remove('sock')
boxes[9].append('battery')
boxes[9].append('vase')

# Put the shark and the rain and the motorcycle into Box 6.
boxes[6].append('shark')
boxes[6].append('rain')
boxes[6].append('motorcycle')

# Put the flower into Box 3.
boxes[3].append('flower')

# Swap the elephant in Box 3 with the table in Box 7.
boxes[3].remove('elephant')
boxes[7].remove('table')
boxes[3].append('table')
boxes[7].append('elephant')

# Put the piano and the candle into Box 8.
boxes[8].append('piano')
boxes[8].append('candle')

# Put the bus into Box 10.
boxes[10].append('bus')

# Swap the toothbrush in Box 7 with the motorcycle in Box 6.
boxes[7].remove('toothbrush')
boxes[6].remove('motorcycle')
boxes[7].append('motorcycle')
boxes[6].append('toothbrush')

# Put the toy into Box 10.
boxes[10].append('toy')

# Replace the belt and the piano and the bicycle with the usb and the river and the frame in Box 5.
boxes[5].remove('belt')
boxes[5].remove('piano')
boxes[5].remove('bicycle')
boxes[5].append('usb')
boxes[5].append('river')
boxes[5].append('frame')

# Move the motorcycle from Box 7 to Box 4.
boxes[7].remove('motorcycle')
boxes[4].append('motorcycle')

# Replace the puzzle and the controller and the wig with the starfish and the glove and the necklace in Box 1.
boxes[1].remove('puzzle')
boxes[1].remove('controller')
boxes[1].remove('wig')
boxes[1].append('starfish')
boxes[1].append('glove')
boxes[1].append('necklace')

# Put the console into Box 8.
boxes[8].append('console')

# Put the rocket into Box 10.
boxes[10].append('rocket')

# Empty Box 3.
boxes[3] = []

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")