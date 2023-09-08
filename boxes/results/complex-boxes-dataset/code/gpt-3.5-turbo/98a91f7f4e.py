# Initial state of boxes
boxes = {
    0: [],
    1: [],
    2: ['glove', 'fish', 'jungle'],
    3: ['tie', 'seaweed', 'clock', 'ocean'],
    4: ['fork', 'meteor', 'pen', 'earring', 'vase'],
    5: ['boat', 'grass', 'freezer'],
    6: ['skirt', 'wallet', 'card'],
    7: [],
    8: ['hat', 'dice', 'brush'],
    9: ['star', 'mixer', 'storm', 'microwave'],
    10: ['usb'],
    11: ['rock', 'scissors', 'bracelet', 'cloud'],
    12: []
}

# Move the glove and the fish from Box 2 to Box 0.
boxes[0].extend(boxes[2].pop(0))
boxes[0].extend(boxes[2].pop(0))

# Remove the pen from Box 4.
boxes[4].remove('pen')

# Replace the boat with the cow in Box 5.
boxes[5].remove('boat')
boxes[5].append('cow')

# Swap the star in Box 9 with the clock in Box 3.
boxes[9].remove('star')
boxes[3].remove('clock')
boxes[9].append('clock')
boxes[3].append('star')

# Put the sculpture into Box 6.
boxes[6].append('sculpture')

# Swap the storm in Box 9 with the grass in Box 5.
boxes[9].remove('storm')
boxes[5].remove('grass')
boxes[9].append('grass')
boxes[5].append('storm')

# Put the branch into Box 5.
boxes[5].append('branch')

# Remove the jungle from Box 2.
boxes[2].remove('jungle')

# Remove the meteor and the earring and the fork from Box 4.
boxes[4].remove('meteor')
boxes[4].remove('earring')
boxes[4].remove('fork')

# Empty Box 4.
boxes[4] = []

# Replace the hat with the desert in Box 8.
boxes[8].remove('hat')
boxes[8].append('desert')

# Remove the star and the tie from Box 3.
boxes[3].remove('star')
boxes[3].remove('tie')

# Remove the glove from Box 0.
boxes[0].remove('glove')

# Move the clock and the grass and the microwave from Box 9 to Box 5.
boxes[9].remove('clock')
boxes[9].remove('grass')
boxes[9].remove('microwave')
boxes[5].extend(['clock', 'grass', 'microwave'])

# Move the wallet from Box 6 to Box 9.
boxes[6].remove('wallet')
boxes[9].append('wallet')

# Replace the branch with the motorcycle in Box 5.
boxes[5].remove('branch')
boxes[5].append('motorcycle')

# Remove the usb from Box 10.
boxes[10].remove('usb')

# Replace the wallet with the fish in Box 9.
boxes[9].remove('wallet')
boxes[9].append('fish')

# Put the hat and the magnet and the rain into Box 7.
boxes[7].extend(['hat', 'magnet', 'rain'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")