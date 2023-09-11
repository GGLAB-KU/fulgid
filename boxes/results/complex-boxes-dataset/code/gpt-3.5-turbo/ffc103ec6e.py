# Initial state of boxes
boxes = {
    0: ['toaster'],
    1: ['sandals', 'dog'],
    2: ['tape'],
    3: ['laptop'],
    4: [],
    5: ['makeup'],
    6: ['headphone', 'drum'],
    7: ['horn', 'butterfly'],
    8: [],
    9: [],
    10: ['pan', 'sock', 'swimsuit', 'oven']
}

# Replace the makeup with the magnet in Box 5.
boxes[5].remove('makeup')
boxes[5].append('magnet')

# Replace the magnet with the shoe in Box 5.
boxes[5].remove('magnet')
boxes[5].append('shoe')

# Swap the drum in Box 6 with the laptop in Box 3.
boxes[6].remove('drum')
boxes[3].remove('laptop')
boxes[6].append('laptop')
boxes[3].append('drum')

# Swap the shoe in Box 5 with the drum in Box 3.
boxes[5].remove('shoe')
boxes[3].remove('drum')
boxes[5].append('drum')
boxes[3].append('shoe')

# Replace the tape with the mirror in Box 2.
boxes[2].remove('tape')
boxes[2].append('mirror')

# Remove the laptop from Box 6.
boxes[6].remove('laptop')

# Swap the sandals in Box 1 with the shoe in Box 3.
boxes[1].remove('sandals')
boxes[3].remove('shoe')
boxes[1].append('shoe')
boxes[3].append('sandals')

# Replace the mirror with the jungle in Box 2.
boxes[2].remove('mirror')
boxes[2].append('jungle')

# Replace the drum with the crown in Box 5.
boxes[5].remove('drum')
boxes[5].append('crown')

# Remove the headphone from Box 6.
boxes[6].remove('headphone')

# Put the razor and the wallet into Box 8.
boxes[8].append('razor')
boxes[8].append('wallet')

# Replace the swimsuit and the oven and the sock with the dolphin and the gloves and the bus in Box 10.
boxes[10].remove('swimsuit')
boxes[10].remove('oven')
boxes[10].remove('sock')
boxes[10].append('dolphin')
boxes[10].append('gloves')
boxes[10].append('bus')

# Move the shoe and the dog from Box 1 to Box 4.
boxes[1].remove('shoe')
boxes[1].remove('dog')
boxes[4].append('shoe')
boxes[4].append('dog')

# Remove the jungle from Box 2.
boxes[2].remove('jungle')

# Move the wallet and the razor from Box 8 to Box 7.
boxes[8].remove('wallet')
boxes[8].remove('razor')
boxes[7].append('wallet')
boxes[7].append('razor')

# Move the dog from Box 4 to Box 3.
boxes[4].remove('dog')
boxes[3].append('dog')

# Move the crown from Box 5 to Box 1.
boxes[5].remove('crown')
boxes[1].append('crown')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")