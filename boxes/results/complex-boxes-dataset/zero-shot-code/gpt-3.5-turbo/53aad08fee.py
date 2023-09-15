box = {
    0: ['lock', 'laptop', 'bus'],
    1: ['beach', 'sock'],
    2: ['boot', 'telescope'],
    3: ['card', 'gloves', 'charger'],
    4: ['rock', 'flower', 'speaker'],
    5: ['truck'],
    6: ['scarf'],
    7: ['wire', 'chair', 'plate', 'microwave'],
    8: ['apple', 'bear', 'puzzle', 'flute', 'tape'],
    9: ['basket', 'toothbrush', 'cloud', 'lamp'],
    10: ['microscope', 'zipper', 'cat', 'shark']
}

def print_boxes():
    for i in range(11):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Move the boot and the telescope from Box 2 to Box 6
box[6].extend(box[2])
del box[2]

# Swap the toothbrush in Box 9 with the lock in Box 0
box[0], box[9] = box[9], box[0]

# Remove the speaker and the rock and the flower from Box 4
del box[4]

# Swap the telescope in Box 6 with the truck in Box 5
box[5], box[6] = box[6], box[5]

# Remove the truck and the scarf and the boot from Box 6
del box[6]

# Remove the beach from Box 1
del box[1]

# Remove the microscope and the shark and the cat from Box 10
del box[10]

# Put the rock and the game and the piano into Box 9
box[9].extend(['rock', 'game', 'piano'])

# Empty Box 1
box[1] = []

# Remove the telescope from Box 5
del box[5]

# Put the bird into Box 10
box[10].append('bird')

# Swap the toothbrush in Box 0 with the game in Box 9
box[0], box[9] = box[9], box[0]

# Move the lock and the lamp from Box 9 to Box 4
box[4].extend([box[9][0], 'lamp'])
del box[9][0]

# Move the bear and the apple and the tape from Box 8 to Box 0
box[0].extend([box[8][1], box[8][0], box[8][4]])
del box[8][0:2]
del box[8][3]

# Remove the charger and the card from Box 3
del box[3][0:2]

# Move the basket and the piano and the cloud from Box 9 to Box 3
box[3].extend([box[9][0], box[9][2], box[9][1]])
del box[9][0:3]

# Move the plate and the microwave and the wire from Box 7 to Box 4
box[4].extend([box[7][2], box[7][3], box[7][0]])
del box[7][0:4]

print_boxes()