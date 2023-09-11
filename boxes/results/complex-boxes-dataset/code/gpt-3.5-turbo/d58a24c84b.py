# Initial state of boxes
boxes = {
    0: ['lightning', 'rocket', 'toothpaste'],
    1: ['star', 'snow', 'butterfly', 'soap', 'puzzle'],
    2: ['ship', 'scarf'],
    3: ['chair'],
    4: [],
    5: [],
    6: ['telescope', 'book', 'boat', 'candle', 'gloves'],
    7: [],
    8: ['crown', 'violin', 'perfume', 'train', 'razor'],
    9: ['glasses', 'makeup', 'guitar'],
    10: ['vase']
}

# Swap the ship in Box 2 with the vase in Box 10.
boxes[2].remove('ship')
boxes[10].remove('vase')
boxes[2].append('vase')
boxes[10].append('ship')

# Put the elephant and the cup into Box 4.
boxes[4].append('elephant')
boxes[4].append('cup')

# Remove the telescope and the book from Box 6.
boxes[6].remove('telescope')
boxes[6].remove('book')

# Move the vase and the scarf from Box 2 to Box 6.
boxes[2].remove('vase')
boxes[2].remove('scarf')
boxes[6].append('vase')
boxes[6].append('scarf')

# Remove the train and the violin and the razor from Box 8.
boxes[8].remove('train')
boxes[8].remove('violin')
boxes[8].remove('razor')

# Put the ship and the octopus and the star into Box 6.
boxes[6].append('ship')
boxes[6].append('octopus')
boxes[6].append('star')

# Remove the gloves from Box 6.
boxes[6].remove('gloves')

# Swap the guitar in Box 9 with the perfume in Box 8.
boxes[9].remove('guitar')
boxes[8].remove('perfume')
boxes[9].append('perfume')
boxes[8].append('guitar')

# Swap the puzzle in Box 1 with the cup in Box 4.
boxes[1].remove('puzzle')
boxes[4].remove('cup')
boxes[1].append('cup')
boxes[4].append('puzzle')

# Put the lamp and the gloves and the bear into Box 0.
boxes[0].append('lamp')
boxes[0].append('gloves')
boxes[0].append('bear')

# Swap the octopus in Box 6 with the guitar in Box 8.
boxes[6].remove('octopus')
boxes[8].remove('guitar')
boxes[6].append('guitar')
boxes[8].append('octopus')

# Replace the chair with the desert in Box 3.
boxes[3].remove('chair')
boxes[3].append('desert')

# Swap the octopus in Box 8 with the puzzle in Box 4.
boxes[8].remove('octopus')
boxes[4].remove('puzzle')
boxes[8].append('puzzle')
boxes[4].append('octopus')

# Swap the octopus in Box 4 with the star in Box 1.
boxes[4].remove('octopus')
boxes[1].remove('star')
boxes[4].append('star')
boxes[1].append('octopus')

# Swap the desert in Box 3 with the ship in Box 10.
boxes[3].remove('desert')
boxes[10].remove('ship')
boxes[3].append('ship')
boxes[10].append('desert')

# Swap the glasses in Box 9 with the desert in Box 10.
boxes[9].remove('glasses')
boxes[10].remove('desert')
boxes[9].append('desert')
boxes[10].append('glasses')

# Replace the glasses with the cloud in Box 10.
boxes[10].remove('glasses')
boxes[10].append('cloud')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")