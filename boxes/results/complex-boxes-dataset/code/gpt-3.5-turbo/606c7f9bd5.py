# Initial state of boxes
boxes = {
    0: ['toy'],
    1: ['microwave', 'coral', 'gloves', 'tiger'],
    2: ['boot'],
    3: [],
    4: ['scissors', 'candle', 'puzzle', 'thread', 'frame'],
    5: ['mirror', 'crown', 'controller', 'pen'],
    6: ['basket', 'shelf', 'wire', 'pan', 'polish'],
    7: ['shorts', 'fish', 'shirt'],
    8: ['bicycle', 'bus', 'magnet'],
    9: ['needle', 'flute', 'bag']
}

# Move the puzzle and the candle from Box 4 to Box 5.
boxes[4].remove('puzzle')
boxes[4].remove('candle')
boxes[5].append('puzzle')
boxes[5].append('candle')

# Swap the bus in Box 8 with the scissors in Box 4.
boxes[8].remove('bus')
boxes[4].remove('scissors')
boxes[8].append('scissors')
boxes[4].append('bus')

# Replace the fish with the mountain in Box 7.
boxes[7].remove('fish')
boxes[7].append('mountain')

# Swap the controller in Box 5 with the toy in Box 0.
boxes[5].remove('controller')
boxes[0].remove('toy')
boxes[5].append('toy')
boxes[0].append('controller')

# Empty Box 0.
boxes[0] = []

# Swap the microwave in Box 1 with the boot in Box 2.
boxes[1].remove('microwave')
boxes[2].remove('boot')
boxes[1].append('boot')
boxes[2].append('microwave')

# Remove the flute from Box 9.
boxes[9].remove('flute')

# Put the toothpaste and the bicycle and the boat into Box 5.
boxes[5].extend(['toothpaste', 'bicycle', 'boat'])

# Swap the microwave in Box 2 with the shelf in Box 6.
boxes[2].remove('microwave')
boxes[6].remove('shelf')
boxes[2].append('shelf')
boxes[6].append('microwave')

# Replace the boat and the mirror with the mask and the usb in Box 5.
boxes[5].remove('boat')
boxes[5].remove('mirror')
boxes[5].append('mask')
boxes[5].append('usb')

# Swap the magnet in Box 8 with the shorts in Box 7.
boxes[8].remove('magnet')
boxes[7].remove('shorts')
boxes[8].append('shorts')
boxes[7].append('magnet')

# Move the bag from Box 9 to Box 8.
boxes[9].remove('bag')
boxes[8].append('bag')

# Put the bicycle and the horse into Box 6.
boxes[6].extend(['bicycle', 'horse'])

# Swap the bag in Box 8 with the frame in Box 4.
boxes[8].remove('bag')
boxes[4].remove('frame')
boxes[8].append('frame')
boxes[4].append('bag')

# Move the bag and the bus from Box 4 to Box 8.
boxes[4].remove('bag')
boxes[4].remove('bus')
boxes[8].append('bag')
boxes[8].append('bus')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")