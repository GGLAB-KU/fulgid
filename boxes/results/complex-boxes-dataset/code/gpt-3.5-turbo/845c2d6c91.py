# Initial state of boxes
boxes = {
    0: ['grinder', 'flute', 'earring', 'battery'],
    1: ['shark', 'cloud', 'table', 'bag', 'helmet'],
    2: [],
    3: ['magnet', 'bowl', 'sandals', 'thunder', 'note'],
    4: ['speaker'],
    5: ['laptop', 'sun', 'bicycle', 'frame'],
    6: ['jacket', 'mask'],
    7: ['tiger', 'car', 'doll', 'gloves'],
    8: [],
    9: ['shelf', 'horse', 'scissors', 'dolphin'],
    10: [],
    11: ['boat', 'forest', 'key', 'watch', 'drum'],
    12: ['spoon', 'rocket', 'fork', 'soap'],
    13: ['comb'],
    14: ['mountain']
}

# Remove the speaker from Box 4.
boxes[4].remove('speaker')

# Move the car from Box 7 to Box 11.
boxes[7].remove('car')
boxes[11].append('car')

# Replace the jacket and the mask with the pen and the moon in Box 6.
boxes[6].remove('jacket')
boxes[6].remove('mask')
boxes[6].append('pen')
boxes[6].append('moon')

# Remove the battery from Box 0.
boxes[0].remove('battery')

# Remove the cloud and the bag from Box 1.
boxes[1].remove('cloud')
boxes[1].remove('bag')

# Remove the watch from Box 11.
boxes[11].remove('watch')

# Replace the table and the shark with the makeup and the harmonica in Box 1.
boxes[1].remove('table')
boxes[1].remove('shark')
boxes[1].append('makeup')
boxes[1].append('harmonica')

# Replace the comb with the note in Box 13.
boxes[13].remove('comb')
boxes[13].append('note')

# Move the pen from Box 6 to Box 7.
boxes[6].remove('pen')
boxes[7].append('pen')

# Swap the mountain in Box 14 with the sun in Box 5.
boxes[14].remove('mountain')
boxes[5].remove('sun')
boxes[14].append('sun')
boxes[5].append('mountain')

# Move the sun from Box 14 to Box 7.
boxes[14].remove('sun')
boxes[7].append('sun')

# Remove the mountain from Box 5.
boxes[5].remove('mountain')

# Empty Box 11.
boxes[11] = []

# Put the oven into Box 12.
boxes[12].append('oven')

# Move the note from Box 13 to Box 0.
boxes[13].remove('note')
boxes[0].append('note')

# Remove the sun from Box 7.
boxes[7].remove('sun')

# Replace the tiger and the gloves and the doll with the vase and the jacket and the sandals in Box 7.
boxes[7].remove('tiger')
boxes[7].remove('gloves')
boxes[7].remove('doll')
boxes[7].append('vase')
boxes[7].append('jacket')
boxes[7].append('sandals')

# Replace the bicycle with the wire in Box 5.
boxes[5].remove('bicycle')
boxes[5].append('wire')

# Remove the helmet from Box 1.
boxes[1].remove('helmet')

# Move the earring from Box 0 to Box 5.
boxes[0].remove('earring')
boxes[5].append('earring')

# Swap the rocket in Box 12 with the shelf in Box 9.
boxes[12].remove('rocket')
boxes[9].remove('shelf')
boxes[12].append('shelf')
boxes[9].append('rocket')

# Swap the sandals in Box 3 with the frame in Box 5.
boxes[3].remove('sandals')
boxes[5].remove('frame')
boxes[3].append('frame')
boxes[5].append('sandals')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")