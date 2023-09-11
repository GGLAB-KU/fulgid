# Initial state of boxes
boxes = {
    0: ['blender'],
    1: ['pan', 'flute'],
    2: ['grinder', 'microscope', 'meteor', 'pants', 'doll'],
    3: ['rock', 'ocean', 'mountain', 'candle'],
    4: ['earring', 'clock', 'lock', 'sun'],
    5: ['bowl'],
    6: ['sculpture']
}

# Swap the blender in Box 0 with the grinder in Box 2.
boxes[0].remove('blender')
boxes[2].remove('grinder')
boxes[0].append('grinder')
boxes[2].append('blender')

# Put the blender and the pan into Box 3.
boxes[3].append('blender')
boxes[3].append('pan')

# Remove the pan and the flute from Box 1.
boxes[1].remove('pan')
boxes[1].remove('flute')

# Replace the sculpture with the gloves in Box 6.
boxes[6].remove('sculpture')
boxes[6].append('gloves')

# Move the pan from Box 3 to Box 0.
boxes[3].remove('pan')
boxes[0].append('pan')

# Remove the earring from Box 4.
boxes[4].remove('earring')

# Replace the pants and the blender with the snow and the horn in Box 2.
boxes[2].remove('pants')
boxes[2].remove('blender')
boxes[2].append('snow')
boxes[2].append('horn')

# Replace the rock and the blender and the mountain with the note and the moon and the octopus in Box 3.
boxes[3].remove('rock')
boxes[3].remove('blender')
boxes[3].remove('mountain')
boxes[3].append('note')
boxes[3].append('moon')
boxes[3].append('octopus')

# Swap the moon in Box 3 with the gloves in Box 6.
boxes[3].remove('moon')
boxes[6].remove('gloves')
boxes[3].append('gloves')
boxes[6].append('moon')

# Put the flute and the gloves and the ring into Box 3.
boxes[3].append('flute')
boxes[3].append('gloves')
boxes[3].append('ring')

# Remove the snow from Box 2.
boxes[2].remove('snow')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")