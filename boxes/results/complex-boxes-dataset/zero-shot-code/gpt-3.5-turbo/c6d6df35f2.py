box = {
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

def print_boxes():
    for i in range(13):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Put the bracelet and the dice and the magnet into Box 0
box[0] += ['bracelet', 'dice', 'magnet']

# Put the laptop and the watch into Box 8
box[8] += ['laptop', 'watch']

# Swap the branch in Box 10 with the keyboard in Box 4
box[10], box[4] = box[4], box[10]

# Swap the ocean in Box 5 with the lightning in Box 9
box[5], box[9] = box[9], box[5]

# Put the gloves and the bus and the moon into Box 12
box[12] += ['gloves', 'bus', 'moon']

# Move the dice from Box 0 to Box 1
box[1].append(box[0].pop(box[0].index('dice')))

# Swap the branch in Box 4 with the keyboard in Box 10
box[4], box[10] = box[10], box[4]

# Swap the motorcycle in Box 5 with the glasses in Box 7
box[5], box[7] = box[7], box[5]

# Swap the bell in Box 12 with the branch in Box 10
box[12], box[10] = box[10], box[12]

# Remove the lightning and the glasses from Box 5
box[5].remove('lightning')
box[5].remove('glasses')

# Move the perfume and the watch from Box 1 to Box 12
box[12] += [box[1].pop(box[1].index('perfume')), box[1].pop(box[1].index('watch'))]

# Move the perfume and the rock from Box 12 to Box 9
box[9] += [box[12].pop(box[12].index('perfume')), box[12].pop(box[12].index('rock'))]

# Replace the horse with the harmonica in Box 6
box[6] = ['harmonica']

# Move the branch from Box 12 to Box 3
box[3].append(box[12].pop(box[12].index('branch')))

# Put the motorcycle into Box 7
box[7].append(box[5].pop(box[5].index('motorcycle')))

# Swap the harmonica in Box 6 with the dice in Box 11
box[6], box[11] = box[11], box[6]

# Put the leaf and the earring into Box 1
box[1] += ['leaf', 'earring']

# Put the paint and the flower and the game into Box 11
box[11] += ['paint', 'flower', 'game']

# Move the leaf and the earring and the star from Box 1 to Box 6
box[6] += [box[1].pop(box[1].index('leaf')), box[1].pop(box[1].index('earring')), box[1].pop(box[1].index('star'))]

# Remove the coin from Box 0
box[0].remove('coin')

# Print the boxes
print_boxes()