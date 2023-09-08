# Initial state of boxes
boxes = {
    0: [],
    1: ['crown', 'keyboard'],
    2: ['makeup', 'flute', 'cow', 'truck'],
    3: ['sock', 'skirt', 'shoe', 'toaster'],
    4: ['pan', 'necklace', 'wig', 'book'],
    5: ['phone', 'scissors'],
    6: ['chair'],
    7: ['battery', 'meteor', 'mountain', 'usb', 'card'],
    8: ['lion', 'toy'],
    9: ['harmonica', 'mask', 'shelf', 'apple', 'belt'],
    10: [],
    11: ['pot', 'umbrella', 'scarf', 'clock', 'swimsuit'],
    12: []
}

# Remove the crown from Box 1.
boxes[1].remove('crown')

# Remove the swimsuit and the clock from Box 11.
boxes[11].remove('swimsuit')
boxes[11].remove('clock')

# Replace the keyboard with the speaker in Box 1.
boxes[1].remove('keyboard')
boxes[1].append('speaker')

# Put the toothbrush into Box 2.
boxes[2].append('toothbrush')

# Empty Box 11.
boxes[11] = []

# Put the blender and the bicycle and the vase into Box 11.
boxes[11].extend(['blender', 'bicycle', 'vase'])

# Move the speaker from Box 1 to Box 0.
boxes[1].remove('speaker')
boxes[0].append('speaker')

# Put the telescope into Box 10.
boxes[10].append('telescope')

# Put the freezer and the bracelet into Box 3.
boxes[3].extend(['freezer', 'bracelet'])

# Replace the flute and the toothbrush with the train and the moon in Box 2.
boxes[2].remove('flute')
boxes[2].remove('toothbrush')
boxes[2].append('train')
boxes[2].append('moon')

# Put the octopus and the jacket and the dice into Box 8.
boxes[8].extend(['octopus', 'jacket', 'dice'])

# Put the octopus into Box 11.
boxes[11].append('octopus')

# Replace the toy and the jacket and the octopus with the key and the wig and the telescope in Box 8.
boxes[8].remove('toy')
boxes[8].remove('jacket')
boxes[8].remove('octopus')
boxes[8].append('key')
boxes[8].append('wig')
boxes[8].append('telescope')

# Remove the usb and the mountain from Box 7.
boxes[7].remove('usb')
boxes[7].remove('mountain')

# Swap the battery in Box 7 with the toaster in Box 3.
boxes[7].remove('battery')
boxes[3].remove('toaster')
boxes[7].append('toaster')
boxes[3].append('battery')

# Swap the telescope in Box 10 with the mask in Box 9.
boxes[10].remove('telescope')
boxes[9].remove('mask')
boxes[10].append('mask')
boxes[9].append('telescope')

# Put the microwave into Box 3.
boxes[3].append('microwave')

# Put the bicycle and the bell into Box 6.
boxes[6].extend(['bicycle', 'bell'])

# Put the polish and the helmet and the lamp into Box 9.
boxes[9].extend(['polish', 'helmet', 'lamp'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")