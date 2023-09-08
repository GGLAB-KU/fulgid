# Initial state of boxes
boxes = {
    0: ['bird'],
    1: ['toothbrush', 'ship', 'butterfly'],
    2: ['rock', 'helmet'],
    3: ['towel', 'wig', 'bag'],
    4: ['horn', 'glove', 'submarine', 'glasses']
}

# Replace the ship and the toothbrush and the butterfly with the polish and the skirt and the razor in Box 1.
boxes[1].remove('ship')
boxes[1].remove('toothbrush')
boxes[1].remove('butterfly')
boxes[1].append('polish')
boxes[1].append('skirt')
boxes[1].append('razor')

# Replace the horn and the glasses and the submarine with the necklace and the jungle and the toaster in Box 4.
boxes[4].remove('horn')
boxes[4].remove('glasses')
boxes[4].remove('submarine')
boxes[4].append('necklace')
boxes[4].append('jungle')
boxes[4].append('toaster')

# Remove the rock from Box 2.
boxes[2].remove('rock')

# Move the bird from Box 0 to Box 3.
boxes[0].remove('bird')
boxes[3].append('bird')

# Put the scarf and the note and the desert into Box 2.
boxes[2].append('scarf')
boxes[2].append('note')
boxes[2].append('desert')

# Remove the polish and the skirt and the razor from Box 1.
boxes[1].remove('polish')
boxes[1].remove('skirt')
boxes[1].remove('razor')

# Remove the helmet from Box 2.
boxes[2].remove('helmet')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")