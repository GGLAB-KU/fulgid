# Initial state of boxes
boxes = {
    0: ['ring', 'paint', 'lamp', 'cup', 'lock'],
    1: ['pot'],
    2: ['forest', 'needle', 'storm'],
    3: ['cloud', 'usb', 'speaker'],
    4: ['toy'],
    5: [],
    6: ['horse', 'island', 'key', 'piano'],
    7: ['towel', 'comb'],
    8: [],
    9: ['horn', 'lion', 'lightning', 'shampoo', 'ocean']
}

# Replace the toy with the whistle in Box 4.
boxes[4].remove('toy')
boxes[4].append('whistle')

# Swap the pot in Box 1 with the usb in Box 3.
boxes[1].remove('pot')
boxes[3].remove('usb')
boxes[1].append('usb')
boxes[3].append('pot')

# Remove the whistle from Box 4.
boxes[4].remove('whistle')

# Put the lock and the bird and the motorcycle into Box 4.
boxes[4].append('lock')
boxes[4].append('bird')
boxes[4].append('motorcycle')

# Put the perfume and the seaweed into Box 0.
boxes[0].append('perfume')
boxes[0].append('seaweed')

# Put the swimsuit and the bus and the flower into Box 1.
boxes[1].append('swimsuit')
boxes[1].append('bus')
boxes[1].append('flower')

# Remove the flower and the usb from Box 1.
boxes[1].remove('flower')
boxes[1].remove('usb')

# Move the bird and the motorcycle from Box 4 to Box 1.
boxes[4].remove('bird')
boxes[4].remove('motorcycle')
boxes[1].append('bird')
boxes[1].append('motorcycle')

# Move the storm and the needle from Box 2 to Box 0.
boxes[2].remove('storm')
boxes[2].remove('needle')
boxes[0].append('storm')
boxes[0].append('needle')

# Empty Box 0.
boxes[0] = []

# Swap the key in Box 6 with the lock in Box 4.
boxes[6].remove('key')
boxes[4].remove('lock')
boxes[6].append('lock')
boxes[4].append('key')

# Move the comb and the towel from Box 7 to Box 1.
boxes[7].remove('comb')
boxes[7].remove('towel')
boxes[1].append('comb')
boxes[1].append('towel')

# Replace the speaker and the pot with the helmet and the wig in Box 3.
boxes[3].remove('speaker')
boxes[3].remove('pot')
boxes[3].append('helmet')
boxes[3].append('wig')

# Swap the lightning in Box 9 with the island in Box 6.
boxes[9].remove('lightning')
boxes[6].remove('island')
boxes[9].append('island')
boxes[6].append('lightning')

# Move the key from Box 4 to Box 0.
boxes[4].remove('key')
boxes[0].append('key')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")