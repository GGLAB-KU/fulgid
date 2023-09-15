box = {
    0: ['truck', 'shampoo'],
    1: ['tree'],
    2: [],
    3: ['motorcycle', 'dice', 'bell'],
    4: ['keyboard', 'shark'],
    5: ['razor'],
    6: ['submarine', 'beach'],
    7: ['thunder'],
    8: [],
    9: ['zipper', 'oven', 'console', 'dress', 'magnet'],
    10: ['violin', 'island', 'ship'],
    11: ['controller', 'cloud', 'rock', 'rain'],
    12: [],
    13: ['pan', 'boat', 'swimsuit']
}

def print_boxes():
    for i in range(14):
        if i in box:
            print(f"Box {i}: {box[i]}")
        else:
            print(f"Box {i}: []")

# Move the magnet from Box 9 to Box 4
box[4].append(box[9].pop(box[9].index('magnet')))

# Replace the shampoo and the truck with the glove and the boot in Box 0
box[0] = ['glove', 'boot']

# Remove the oven and the console and the zipper from Box 9
box[9] = [item for item in box[9] if item not in ['oven', 'console', 'zipper']]

# Put the submarine into Box 11
box[11].append(box[6].pop(box[6].index('submarine')))

# Remove the razor from Box 5
box[5].remove('razor')

# Move the dress from Box 9 to Box 1
box[1].append(box[9].pop(box[9].index('dress')))

# Remove the keyboard from Box 4
box[4].remove('keyboard')

# Replace the dress with the lock in Box 1
box[1] = ['lock']

# Replace the lock with the star in Box 1
box[1] = ['star']

# Remove the controller and the cloud and the submarine from Box 11
box[11] = [item for item in box[11] if item not in ['controller', 'cloud', 'submarine']]

# Move the star from Box 1 to Box 3
box[3].append(box[1].pop(box[1].index('star')))

# Swap the ship in Box 10 with the dice in Box 3
box[3].append(box[10].pop(box[10].index('dice')))
box[10].append(box[3].pop(box[3].index('ship')))

# Move the boot and the glove from Box 0 to Box 5
box[5].extend(box[0])
box[0] = []

# Replace the dice and the violin with the meteor and the bicycle in Box 10
box[10] = ['meteor', 'bicycle']

# Swap the submarine in Box 6 with the tree in Box 1
box[1].append(box[6].pop(box[6].index('tree')))
box[6].append(box[1].pop(box[1].index('submarine')))

# Move the beach from Box 6 to Box 3
box[3].append(box[6].pop(box[6].index('beach')))

# Remove the glove from Box 5
box[5].remove('glove')

# Remove the rock and the rain from Box 11
box[11] = [item for item in box[11] if item not in ['rock', 'rain']]

# Move the ship and the motorcycle from Box 3 to Box 8
box[8].extend(box[3])
box[3] = []

# Move the bicycle and the island and the meteor from Box 10 to Box 3
box[3].extend(box[10])
box[10] = []

# Put the shampoo into Box 12
box[12].append(box[0].pop(box[0].index('shampoo')))

print_boxes()