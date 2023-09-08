# Initial state of boxes
boxes = {
    0: ['ring', 'shoe'],
    1: ['tape'],
    2: [],
    3: [],
    4: ['pot', 'submarine', 'rock', 'laptop'],
    5: ['wig', 'usb', 'bus', 'toothpaste'],
    6: [],
    7: ['skirt', 'cat', 'razor', 'freezer', 'mirror'],
    8: ['hat', 'telescope', 'sock', 'bird', 'speaker']
}

# Replace the submarine and the pot with the harmonica and the horse in Box 4.
boxes[4].remove('submarine')
boxes[4].remove('pot')
boxes[4].append('harmonica')
boxes[4].append('horse')

# Replace the tape with the seaweed in Box 1.
boxes[1].remove('tape')
boxes[1].append('seaweed')

# Put the usb and the microwave into Box 0.
boxes[0].append('usb')
boxes[0].append('microwave')

# Swap the freezer in Box 7 with the ring in Box 0.
boxes[7].remove('freezer')
boxes[0].remove('ring')
boxes[7].append('ring')
boxes[0].append('freezer')

# Put the wire and the truck and the pants into Box 5.
boxes[5].append('wire')
boxes[5].append('truck')
boxes[5].append('pants')

# Replace the seaweed with the bell in Box 1.
boxes[1].remove('seaweed')
boxes[1].append('bell')

# Remove the hat and the telescope and the speaker from Box 8.
boxes[8].remove('hat')
boxes[8].remove('telescope')
boxes[8].remove('speaker')

# Replace the pants and the truck with the sock and the jungle in Box 5.
boxes[5].remove('pants')
boxes[5].remove('truck')
boxes[5].append('sock')
boxes[5].append('jungle')

# Empty Box 7.
boxes[7] = []

# Swap the bird in Box 8 with the usb in Box 5.
boxes[8].remove('bird')
boxes[5].remove('usb')
boxes[8].append('usb')
boxes[5].append('bird')

# Move the bell from Box 1 to Box 8.
boxes[1].remove('bell')
boxes[8].append('bell')

# Put the ship into Box 1.
boxes[1].append('ship')

# Put the star and the island into Box 5.
boxes[5].append('star')
boxes[5].append('island')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")