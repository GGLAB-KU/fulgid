# Initial state of boxes
boxes = {
    0: ['storm'],
    1: ['cloud'],
    2: [],
    3: ['moon'],
    4: ['mask', 'lightning'],
    5: ['helmet', 'fish', 'pants', 'desert', 'rain'],
    6: ['shirt', 'beach', 'perfume', 'clock', 'tape'],
    7: ['plane', 'microscope', 'magnet'],
    8: ['usb'],
    9: ['train', 'towel', 'mountain', 'brush']
}

# Move the lightning and the mask from Box 4 to Box 3.
boxes[4].remove('lightning')
boxes[4].remove('mask')
boxes[3].append('lightning')
boxes[3].append('mask')

# Replace the usb with the table in Box 8.
boxes[8].remove('usb')
boxes[8].append('table')

# Replace the cloud with the rock in Box 1.
boxes[1].remove('cloud')
boxes[1].append('rock')

# Remove the storm from Box 0.
boxes[0].remove('storm')

# Empty Box 9.
boxes[9] = []

# Move the plane and the magnet from Box 7 to Box 6.
boxes[7].remove('plane')
boxes[7].remove('magnet')
boxes[6].append('plane')
boxes[6].append('magnet')

# Remove the table from Box 8.
boxes[8].remove('table')

# Replace the rock with the table in Box 1.
boxes[1].remove('rock')
boxes[1].append('table')

# Replace the desert and the helmet and the pants with the flute and the jacket and the fork in Box 5.
boxes[5].remove('desert')
boxes[5].remove('helmet')
boxes[5].remove('pants')
boxes[5].append('flute')
boxes[5].append('jacket')
boxes[5].append('fork')

# Put the shark and the bell into Box 5.
boxes[5].append('shark')
boxes[5].append('bell')

# Remove the tape from Box 6.
boxes[6].remove('tape')

# Remove the lightning from Box 3.
boxes[3].remove('lightning')

# Replace the microscope with the controller in Box 7.
boxes[7].remove('microscope')
boxes[7].append('controller')

# Put the grass and the pot into Box 6.
boxes[6].append('grass')
boxes[6].append('pot')

# Remove the controller from Box 7.
boxes[7].remove('controller')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")