# Initial state of boxes
boxes = {
    0: ['chair', 'bus', 'butterfly', 'bell'],
    1: ['earring', 'lightning'],
    2: ['watch', 'violin'],
    3: [],
    4: ['flute'],
    5: ['telescope'],
    6: ['swimsuit', 'belt', 'horn']
}

# Move the telescope from Box 5 to Box 0.
boxes[5].remove('telescope')
boxes[0].append('telescope')

# Move the flute from Box 4 to Box 0.
boxes[4].remove('flute')
boxes[0].append('flute')

# Move the bus from Box 0 to Box 6.
boxes[0].remove('bus')
boxes[6].append('bus')

# Remove the belt from Box 6.
boxes[6].remove('belt')

# Remove the bell and the flute from Box 0.
boxes[0].remove('bell')
boxes[0].remove('flute')

# Put the bicycle into Box 2.
boxes[2].append('bicycle')

# Remove the violin and the bicycle and the watch from Box 2.
boxes[2].remove('violin')
boxes[2].remove('bicycle')
boxes[2].remove('watch')

# Remove the earring from Box 1.
boxes[1].remove('earring')

# Replace the chair and the telescope and the butterfly with the shoe and the submarine and the mountain in Box 0.
boxes[0].remove('chair')
boxes[0].remove('telescope')
boxes[0].remove('butterfly')
boxes[0].append('shoe')
boxes[0].append('submarine')
boxes[0].append('mountain')

# Put the belt into Box 4.
boxes[4].append('belt')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")