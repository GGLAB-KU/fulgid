boxes = {
    0: ['makeup', 'card', 'cloud', 'magnet', 'toothpaste'],
    1: ['toaster'],
    2: ['river', 'glove'],
    3: ['sun', 'meteor'],
    4: ['car'],
    5: ['coral', 'tree', 'necklace'],
    6: ['pan', 'paint'],
    7: [],
    8: ['boat', 'comb'],
    9: ['star', 'whistle'],
    10: [],
    11: ['sandals', 'desert', 'battery', 'needle']
}

def print_boxes():
    for box, items in boxes.items():
        print(f"Box {box}: {items}")

# Put the comb into Box 6
boxes[6].append('comb')

# Move the river from Box 2 to Box 9
boxes[9].append(boxes[2].pop(boxes[2].index('river')))

# Move the sun from Box 3 to Box 11
boxes[11].append(boxes[3].pop(boxes[3].index('sun')))

# Put the rock into Box 4
boxes[4].append('rock')

# Swap the boat in Box 8 with the sun in Box 11
boxes[8].append(boxes[11].pop(boxes[11].index('sun')))
boxes[11].append(boxes[8].pop(boxes[8].index('boat')))

# Swap the toaster in Box 1 with the glove in Box 2
boxes[1].append(boxes[2].pop(boxes[2].index('glove')))
boxes[2].append(boxes[1].pop(boxes[1].index('toaster')))

# Put the piano and the speaker and the tree into Box 10
boxes[10].extend(['piano', 'speaker', 'tree'])

# Put the skirt into Box 8
boxes[8].append('skirt')

# Put the beach and the pen and the doll into Box 5
boxes[5].extend(['beach', 'pen', 'doll'])

# Move the car and the rock from Box 4 to Box 10
boxes[10].extend([boxes[4].pop(boxes[4].index('car')), boxes[4].pop(boxes[4].index('rock'))])

# Move the coral and the beach and the necklace from Box 5 to Box 11
boxes[11].extend([boxes[5].pop(boxes[5].index('coral')), boxes[5].pop(boxes[5].index('beach')), boxes[5].pop(boxes[5].index('necklace'))])

# Move the glove from Box 1 to Box 5
boxes[5].append(boxes[1].pop(boxes[1].index('glove')))

# Remove the paint and the pan and the comb from Box 6
boxes[6].remove('paint')
boxes[6].remove('pan')
boxes[6].remove('comb')

# Move the glove and the doll and the pen from Box 5 to Box 0
boxes[0].extend([boxes[5].pop(boxes[5].index('glove')), boxes[5].pop(boxes[5].index('doll')), boxes[5].pop(boxes[5].index('pen'))])

# Move the tree from Box 5 to Box 6
boxes[6].append(boxes[5].pop(boxes[5].index('tree')))

# Put the lion and the magnet and the shirt into Box 2
boxes[2].extend(['lion', 'magnet', 'shirt'])

# Swap the speaker in Box 10 with the toothpaste in Box 0
boxes[0].append(boxes[10].pop(boxes[10].index('toothpaste')))
boxes[10].append(boxes[0].pop(boxes[0].index('speaker')))

# Put the dress and the bag into Box 4
boxes[4].extend(['dress', 'bag'])

# Print the final state of the boxes
print_boxes()