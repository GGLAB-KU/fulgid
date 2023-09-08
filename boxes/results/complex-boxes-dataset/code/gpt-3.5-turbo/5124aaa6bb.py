# Initial state of boxes
boxes = {
    0: [],
    1: ['octopus'],
    2: [],
    3: [],
    4: ['mountain', 'freezer', 'basket'],
    5: ['cup', 'bird', 'gloves', 'forest'],
    6: [],
    7: ['fork', 'planet'],
    8: ['leaf', 'usb', 'note', 'rocket', 'toothpaste'],
    9: [],
    10: ['motorcycle', 'hat', 'lion'],
    11: [],
    12: ['moon'],
    13: ['spoon', 'zipper']
}

# Put the chair and the plane and the lamp into Box 12.
boxes[12].extend(['chair', 'plane', 'lamp'])

# Replace the toothpaste and the leaf and the note with the mask and the telescope and the beach in Box 8.
boxes[8].remove('toothpaste')
boxes[8].remove('leaf')
boxes[8].remove('note')
boxes[8].append('mask')
boxes[8].append('telescope')
boxes[8].append('beach')

# Put the grass into Box 4.
boxes[4].append('grass')

# Move the mask from Box 8 to Box 3.
boxes[8].remove('mask')
boxes[3].append('mask')

# Remove the mask from Box 3.
boxes[3].remove('mask')

# Replace the zipper with the lock in Box 13.
boxes[13].remove('zipper')
boxes[13].append('lock')

# Replace the octopus with the sun in Box 1.
boxes[1].remove('octopus')
boxes[1].append('sun')

# Put the headphone and the razor and the necklace into Box 12.
boxes[12].extend(['headphone', 'razor', 'necklace'])

# Swap the usb in Box 8 with the cup in Box 5.
boxes[8].remove('usb')
boxes[5].remove('cup')
boxes[8].append('cup')
boxes[5].append('usb')

# Replace the chair and the headphone with the whistle and the ocean in Box 12.
boxes[12].remove('chair')
boxes[12].remove('headphone')
boxes[12].append('whistle')
boxes[12].append('ocean')

# Remove the rocket from Box 8.
boxes[8].remove('rocket')

# Swap the planet in Box 7 with the lock in Box 13.
boxes[7].remove('planet')
boxes[13].remove('lock')
boxes[7].append('lock')
boxes[13].append('planet')

# Put the console and the pants into Box 7.
boxes[7].extend(['console', 'pants'])

# Move the sun from Box 1 to Box 0.
boxes[1].remove('sun')
boxes[0].append('sun')

# Move the usb and the bird and the forest from Box 5 to Box 1.
boxes[5].remove('usb')
boxes[5].remove('bird')
boxes[5].remove('forest')
boxes[1].append('usb')
boxes[1].append('bird')
boxes[1].append('forest')

# Remove the planet and the spoon from Box 13.
boxes[13].remove('planet')
boxes[13].remove('spoon')

# Move the motorcycle and the lion from Box 10 to Box 11.
boxes[10].remove('motorcycle')
boxes[10].remove('lion')
boxes[11].extend(['motorcycle', 'lion'])

# Swap the console in Box 7 with the hat in Box 10.
boxes[7].remove('console')
boxes[10].remove('hat')
boxes[7].append('hat')
boxes[10].append('console')

# Swap the lion in Box 11 with the telescope in Box 8.
boxes[11].remove('lion')
boxes[8].remove('telescope')
boxes[11].append('telescope')
boxes[8].append('lion')

# Put the beach and the blanket into Box 4.
boxes[4].extend(['beach', 'blanket'])

# Put the horn and the usb into Box 1.
boxes[1].extend(['horn', 'usb'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")