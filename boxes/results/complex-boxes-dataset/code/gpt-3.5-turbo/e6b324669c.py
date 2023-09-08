# Initial state of boxes
boxes = {
    0: ['keyboard', 'planet', 'razor', 'scissors'],
    1: ['frame', 'battery', 'blanket', 'fish', 'watch'],
    2: ['seaweed', 'fork', 'sculpture', 'belt', 'ocean'],
    3: ['jungle', 'glasses', 'swimsuit', 'camera'],
    4: ['pen', 'toy'],
    5: ['tape', 'tree', 'microscope', 'table', 'submarine'],
    6: ['speaker', 'shirt', 'card', 'note', 'comet'],
    7: ['leaf', 'mixer', 'octopus'],
    8: ['island', 'apple', 'controller', 'wire'],
    9: ['helmet'],
    10: ['scarf', 'train'],
    11: ['doll', 'umbrella', 'bag', 'chair', 'harmonica'],
    12: ['headphone', 'charger', 'shampoo', 'shark'],
    13: ['coin', 'hat', 'flute', 'lamp', 'sock'],
    14: ['dice', 'beach', 'jacket']
}

# Put the skirt and the sandals and the button into Box 9.
boxes[9].extend(['skirt', 'sandals', 'button'])

# Put the piano into Box 8.
boxes[8].append('piano')

# Put the crown and the laptop and the bowl into Box 7.
boxes[7].extend(['crown', 'laptop', 'bowl'])

# Put the cat and the tree into Box 5.
boxes[5].extend(['cat', 'tree'])

# Put the microscope and the river into Box 4.
boxes[4].extend(['microscope', 'river'])

# Put the rock and the meteor and the headphone into Box 5.
boxes[5].extend(['rock', 'meteor', 'headphone'])

# Put the battery and the rain into Box 10.
boxes[10].extend(['battery', 'rain'])

# Move the helmet and the sandals from Box 9 to Box 5.
boxes[9].remove('helmet')
boxes[9].remove('sandals')
boxes[5].extend(['helmet', 'sandals'])

# Move the laptop and the crown from Box 7 to Box 14.
boxes[7].remove('laptop')
boxes[7].remove('crown')
boxes[14].extend(['laptop', 'crown'])

# Move the submarine and the meteor from Box 5 to Box 7.
boxes[5].remove('submarine')
boxes[5].remove('meteor')
boxes[7].extend(['submarine', 'meteor'])

# Put the car and the shampoo and the motorcycle into Box 5.
boxes[5].extend(['car', 'shampoo', 'motorcycle'])

# Empty Box 1.
boxes[1] = []

# Remove the battery and the scarf and the train from Box 10.
boxes[10].remove('battery')
boxes[10].remove('scarf')
boxes[10].remove('train')

# Put the bag into Box 1.
boxes[1].append('bag')

# Move the river and the pen and the toy from Box 4 to Box 0.
boxes[4].remove('river')
boxes[4].remove('pen')
boxes[4].remove('toy')
boxes[0].extend(['river', 'pen', 'toy'])

# Put the brush into Box 11.
boxes[11].append('brush')

# Move the table from Box 5 to Box 2.
boxes[5].remove('table')
boxes[2].append('table')

# Put the telescope and the bus into Box 6.
boxes[6].extend(['telescope', 'bus'])

# Move the beach and the laptop from Box 14 to Box 2.
boxes[14].remove('beach')
boxes[14].remove('laptop')
boxes[2].extend(['beach', 'laptop'])

# Put the glove and the coral into Box 7.
boxes[7].extend(['glove', 'coral'])

# Move the beach from Box 2 to Box 6.
boxes[2].remove('beach')
boxes[6].append('beach')

# Replace the comet and the card with the grinder and the button in Box 6.
boxes[6].remove('comet')
boxes[6].remove('card')
boxes[6].extend(['grinder', 'button'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")