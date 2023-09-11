# Initial state of boxes
boxes = {
    0: ['headphone', 'coin'],
    1: ['star', 'perfume', 'watch'],
    2: [],
    3: ['snow'],
    4: ['toy', 'keyboard'],
    5: ['motorcycle', 'ocean'],
    6: ['horse'],
    7: ['glasses', 'charger', 'console', 'leaf', 'card'],
    8: ['crown', 'desert', 'game', 'dress', 'thunder'],
    9: ['island', 'pants', 'car', 'pen', 'lightning'],
    10: ['branch'],
    11: ['dice', 'fridge', 'spoon', 'belt', 'table'],
    12: ['mask', 'rock', 'bell']
}

# Put the bracelet and the dice and the magnet into Box 0.
boxes[0].extend(['bracelet', 'dice', 'magnet'])

# Put the laptop and the watch into Box 8.
boxes[8].extend(['laptop', 'watch'])

# Swap the branch in Box 10 with the keyboard in Box 4.
boxes[10], boxes[4] = boxes[4], boxes[10]

# Swap the ocean in Box 5 with the lightning in Box 9.
boxes[5], boxes[9] = boxes[9], boxes[5]

# Put the gloves and the bus and the moon into Box 12.
boxes[12].extend(['gloves', 'bus', 'moon'])

# Move the dice from Box 0 to Box 1.
boxes[0].remove('dice')
boxes[1].append('dice')

# Swap the branch in Box 4 with the keyboard in Box 10.
boxes[4], boxes[10] = boxes[10], boxes[4]

# Swap the motorcycle in Box 5 with the glasses in Box 7.
boxes[5], boxes[7] = boxes[7], boxes[5]

# Swap the bell in Box 12 with the branch in Box 10.
boxes[12], boxes[10] = boxes[10], boxes[12]

# Remove the lightning and the glasses from Box 5.
boxes[5].remove('lightning')
boxes[5].remove('glasses')

# Move the perfume and the watch from Box 1 to Box 12.
boxes[1].remove('perfume')
boxes[1].remove('watch')
boxes[12].extend(['perfume', 'watch'])

# Move the perfume and the rock from Box 12 to Box 9.
boxes[12].remove('perfume')
boxes[12].remove('rock')
boxes[9].extend(['perfume', 'rock'])

# Replace the horse with the harmonica in Box 6.
boxes[6].remove('horse')
boxes[6].append('harmonica')

# Move the branch from Box 12 to Box 3.
boxes[12].remove('branch')
boxes[3].append('branch')

# Put the motorcycle into Box 7.
boxes[7].append('motorcycle')

# Swap the harmonica in Box 6 with the dice in Box 11.
boxes[6], boxes[11] = boxes[11], boxes[6]

# Put the leaf and the earring into Box 1.
boxes[1].extend(['leaf', 'earring'])

# Put the paint and the flower and the game into Box 11.
boxes[11].extend(['paint', 'flower', 'game'])

# Move the leaf and the earring and the star from Box 1 to Box 6.
boxes[1].remove('leaf')
boxes[1].remove('earring')
boxes[1].remove('star')
boxes[6].extend(['leaf', 'earring', 'star'])

# Remove the coin from Box 0.
boxes[0].remove('coin')

# Print the boxes
for box_number, items in boxes.items():
    print(f"Box {box_number}: {items}")