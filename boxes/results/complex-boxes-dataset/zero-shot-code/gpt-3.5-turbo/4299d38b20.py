box = {
    0: ['perfume', 'wallet', 'blender'],
    1: [],
    2: ['horse', 'mountain', 'ring'],
    3: ['skirt', 'pants', 'toothpaste', 'brush'],
    4: ['rock', 'bag', 'coin', 'game'],
    5: [],
    6: ['soap', 'gloves', 'guitar'],
    7: ['apple', 'toy'],
    8: ['ship', 'grass', 'pen', 'storm', 'rocket'],
    9: ['bicycle', 'makeup', 'console', 'sandals'],
    10: ['lion', 'frame'],
    11: []
}

# Move the apple and the toy from Box 7 to Box 0
box[0].extend(box[7])
box[7] = []

# Remove the ship and the pen from Box 8
box[8].remove('ship')
box[8].remove('pen')

# Move the brush and the skirt and the pants from Box 3 to Box 0
box[0].extend(box[3])
box[3] = []

# Swap the soap in Box 6 with the frame in Box 10
box[6], box[10] = box[10], box[6]

# Remove the gloves from Box 6
box[6].remove('gloves')

# Put the zipper and the tiger into Box 11
box[11].extend(['zipper', 'tiger'])

# Put the shoe and the table into Box 9
box[9].extend(['shoe', 'table'])

# Remove the lion from Box 10
box[10].remove('lion')

# Move the rocket and the grass from Box 8 to Box 10
box[10].extend(['rocket', 'grass'])
box[8].remove('rocket')
box[8].remove('grass')

# Replace the horse and the ring with the sandals and the plane in Box 2
box[2] = ['sandals', 'plane']

# Move the wallet and the apple from Box 0 to Box 5
box[5].extend(['wallet', 'apple'])
box[0].remove('wallet')
box[0].remove('apple')

# Swap the storm in Box 8 with the apple in Box 5
box[5].remove('apple')
box[5].append('storm')
box[8].remove('storm')
box[8].append('apple')

# Replace the guitar and the frame with the magnet and the tree in Box 6
box[6] = ['magnet', 'tree']

# Replace the grass and the soap with the pillow and the comet in Box 10
box[10] = ['pillow', 'comet']

# Swap the apple in Box 8 with the console in Box 9
box[8].remove('apple')
box[9].remove('console')
box[8].append('console')
box[9].append('apple')

# Put the towel and the lamp and the train into Box 2
box[2].extend(['towel', 'lamp', 'train'])

# Remove the pants from Box 0
box[0].remove('pants')

# Put the sandals and the gloves into Box 5
box[5].extend(['sandals', 'gloves'])

# Print the contents of each box
for i in range(12):
    print(f"Box {i}: {box[i]}")