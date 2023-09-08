# Initial state of boxes
boxes = {
    0: ['wire'],
    1: ['whistle'],
    2: ['cow', 'watch'],
    3: [],
    4: ['fridge'],
    5: ['dolphin', 'usb'],
    6: ['rain', 'meteor', 'toothbrush'],
    7: ['tape', 'magnet', 'motorcycle'],
    8: ['branch'],
    9: ['towel', 'phone'],
    10: ['mirror', 'mask', 'controller', 'ship', 'wallet'],
    11: ['bus'],
    12: ['forest', 'snow'],
    13: ['leaf'],
    14: ['soap']
}

# Put the blanket and the doll and the clock into Box 3.
boxes[3].extend(['blanket', 'doll', 'clock'])

# Replace the wire with the bus in Box 0.
boxes[0].remove('wire')
boxes[0].append('bus')

# Remove the magnet from Box 7.
boxes[7].remove('magnet')

# Swap the fridge in Box 4 with the mirror in Box 10.
boxes[4].remove('fridge')
boxes[10].remove('mirror')
boxes[4].append('mirror')
boxes[10].append('fridge')

# Remove the bus from Box 11.
boxes[11].remove('bus')

# Remove the comb from Box 3.
boxes[3].remove('comb')

# Put the jungle and the forest and the soap into Box 10.
boxes[10].extend(['jungle', 'forest', 'soap'])

# Remove the watch from Box 2.
boxes[2].remove('watch')

# Swap the tape in Box 7 with the dolphin in Box 5.
boxes[7].remove('tape')
boxes[5].remove('dolphin')
boxes[7].append('dolphin')
boxes[5].append('tape')

# Swap the leaf in Box 13 with the cow in Box 2.
boxes[13].remove('leaf')
boxes[2].remove('cow')
boxes[13].append('cow')
boxes[2].append('leaf')

# Remove the mirror from Box 4.
boxes[4].remove('mirror')

# Replace the clock with the hat in Box 3.
boxes[3].remove('clock')
boxes[3].append('hat')

# Move the toothbrush from Box 6 to Box 5.
boxes[6].remove('toothbrush')
boxes[5].append('toothbrush')

# Move the branch from Box 8 to Box 11.
boxes[8].remove('branch')
boxes[11].append('branch')

# Empty Box 0.
boxes[0] = []

# Move the branch from Box 11 to Box 1.
boxes[11].remove('branch')
boxes[1].append('branch')

# Move the dolphin from Box 7 to Box 6.
boxes[7].remove('dolphin')
boxes[6].append('dolphin')

# Replace the motorcycle with the swimsuit in Box 7.
boxes[7].remove('motorcycle')
boxes[7].append('swimsuit')

# Put the note into Box 12.
boxes[12].append('note')

# Put the zipper into Box 7.
boxes[7].append('zipper')

# Move the zipper and the swimsuit from Box 7 to Box 12.
boxes[7].remove('zipper')
boxes[7].remove('swimsuit')
boxes[12].extend(['zipper', 'swimsuit'])

# Swap the dolphin in Box 6 with the towel in Box 9.
boxes[6].remove('dolphin')
boxes[9].remove('towel')
boxes[6].append('towel')
boxes[9].append('dolphin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")