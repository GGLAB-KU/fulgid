# Initial state of boxes
boxes = {
    0: ['branch', 'starfish', 'plane', 'pen', 'jungle'],
    1: ['usb'],
    2: ['zipper'],
    3: ['soap', 'telescope'],
    4: ['pan', 'paint'],
    5: ['basket', 'shorts'],
    6: [],
    7: ['sock', 'toaster'],
    8: ['seaweed', 'sun', 'table'],
    9: [],
    10: ['meteor', 'microscope'],
    11: ['train', 'laptop', 'perfume', 'scarf'],
    12: ['rocket', 'bag', 'lock', 'lightning', 'speaker']
}

# Swap the usb in Box 1 with the telescope in Box 3.
boxes[1].remove('usb')
boxes[3].remove('telescope')
boxes[1].append('telescope')
boxes[3].append('usb')

# Put the shorts into Box 10.
boxes[10].append('shorts')

# Remove the shorts and the basket from Box 5.
boxes[5].remove('shorts')
boxes[5].remove('basket')

# Put the rain and the ring and the desert into Box 8.
boxes[8].append('rain')
boxes[8].append('ring')
boxes[8].append('desert')

# Remove the bag from Box 12.
boxes[12].remove('bag')

# Move the shorts and the meteor from Box 10 to Box 5.
boxes[10].remove('shorts')
boxes[10].remove('meteor')
boxes[5].append('shorts')
boxes[5].append('meteor')

# Remove the telescope from Box 1.
boxes[1].remove('telescope')

# Put the bag and the note and the boat into Box 4.
boxes[4].append('bag')
boxes[4].append('note')
boxes[4].append('boat')

# Put the magnet and the key and the cat into Box 12.
boxes[12].append('magnet')
boxes[12].append('key')
boxes[12].append('cat')

# Replace the magnet with the laptop in Box 12.
boxes[12].remove('magnet')
boxes[12].append('laptop')

# Replace the perfume and the scarf with the shorts and the motorcycle in Box 11.
boxes[11].remove('perfume')
boxes[11].remove('scarf')
boxes[11].append('shorts')
boxes[11].append('motorcycle')

# Put the blanket and the shorts into Box 4.
boxes[4].append('blanket')
boxes[4].append('shorts')

# Replace the pen and the plane and the jungle with the ocean and the car and the console in Box 0.
boxes[0].remove('pen')
boxes[0].remove('plane')
boxes[0].remove('jungle')
boxes[0].append('ocean')
boxes[0].append('car')
boxes[0].append('console')

# Remove the sun and the rain from Box 8.
boxes[8].remove('sun')
boxes[8].remove('rain')

# Remove the speaker and the lock from Box 12.
boxes[12].remove('speaker')
boxes[12].remove('lock')

# Remove the soap and the usb from Box 3.
boxes[3].remove('soap')
boxes[3].remove('usb')

# Empty Box 7.
boxes[7] = []

# Remove the shorts and the meteor from Box 5.
boxes[5].remove('shorts')
boxes[5].remove('meteor')

# Move the shorts and the motorcycle from Box 11 to Box 0.
boxes[11].remove('shorts')
boxes[11].remove('motorcycle')
boxes[0].append('shorts')
boxes[0].append('motorcycle')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")