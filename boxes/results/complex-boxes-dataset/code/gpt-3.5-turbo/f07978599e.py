# Initial state of boxes
boxes = {
    0: ['thunder', 'shark', 'needle', 'pen', 'truck'],
    1: ['scissors', 'earring', 'lamp'],
    2: ['lion', 'frame'],
    3: ['pan', 'forest', 'watch', 'flute'],
    4: ['helmet', 'car'],
    5: ['comb', 'gloves', 'telescope', 'ring', 'horn'],
    6: ['tiger', 'battery'],
    7: [],
    8: ['storm', 'plane', 'coat'],
    9: ['starfish', 'jacket', 'motorcycle'],
    10: ['elephant', 'cat', 'thread'],
    11: [],
    12: ['lightning', 'octopus', 'flower', 'mountain', 'apple'],
    13: ['piano', 'clock', 'mirror', 'seaweed']
}

# Put the book and the drum and the mixer into Box 3.
boxes[3].extend(['book', 'drum', 'mixer'])

# Put the polish and the ring into Box 10.
boxes[10].extend(['polish', 'ring'])

# Remove the scissors from Box 1.
boxes[1].remove('scissors')

# Remove the apple from Box 12.
boxes[12].remove('apple')

# Remove the frame from Box 2.
boxes[2].remove('frame')

# Swap the car in Box 4 with the octopus in Box 12.
boxes[4].remove('car')
boxes[12].remove('octopus')
boxes[4].append('octopus')
boxes[12].append('car')

# Remove the coat and the storm from Box 8.
boxes[8].remove('coat')
boxes[8].remove('storm')

# Put the ocean and the bus and the necklace into Box 9.
boxes[9].extend(['ocean', 'bus', 'necklace'])

# Remove the lamp and the earring from Box 1.
boxes[1].remove('lamp')
boxes[1].remove('earring')

# Put the octopus and the motorcycle into Box 10.
boxes[10].extend(['octopus', 'motorcycle'])

# Replace the plane with the cloud in Box 8.
boxes[8].remove('plane')
boxes[8].append('cloud')

# Put the brush into Box 3.
boxes[3].append('brush')

# Move the gloves and the horn from Box 5 to Box 2.
boxes[5].remove('gloves')
boxes[5].remove('horn')
boxes[2].extend(['gloves', 'horn'])

# Swap the lion in Box 2 with the tiger in Box 6.
boxes[2].remove('lion')
boxes[6].remove('tiger')
boxes[2].append('tiger')
boxes[6].append('lion')

# Move the ring from Box 10 to Box 1.
boxes[10].remove('ring')
boxes[1].append('ring')

# Remove the ring from Box 1.
boxes[1].remove('ring')

# Replace the mountain with the pot in Box 12.
boxes[12].remove('mountain')
boxes[12].append('pot')

# Remove the lightning and the flower from Box 12.
boxes[12].remove('lightning')
boxes[12].remove('flower')

# Move the flute and the brush from Box 3 to Box 4.
boxes[3].remove('flute')
boxes[3].remove('brush')
boxes[4].extend(['flute', 'brush'])

# Remove the mixer and the watch and the book from Box 3.
boxes[3].remove('mixer')
boxes[3].remove('watch')
boxes[3].remove('book')

# Put the butterfly and the microwave into Box 9.
boxes[9].extend(['butterfly', 'microwave'])

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")