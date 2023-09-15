box_0 = ['rock', 'flute', 'violin', 'camera']
box_1 = ['game', 'earring', 'watch', 'rocket']
box_2 = ['sun', 'grass', 'toy']
box_3 = ['key', 'clock', 'rain', 'tree']
box_4 = ['island', 'freezer', 'sculpture']
box_5 = []
box_6 = []
box_7 = ['seaweed', 'doll', 'beach', 'jungle']
box_8 = []
box_9 = ['phone', 'comb', 'laptop', 'toothbrush']

# Put the earring and the mixer into Box 9
box_9.extend(['earring', 'mixer'])

# Put the table and the glasses into Box 1
box_1.extend(['table', 'glasses'])

# Put the shorts and the bell and the truck into Box 0
box_0.extend(['shorts', 'bell', 'truck'])

# Move the game and the watch from Box 1 to Box 6
box_6.extend([box_1.pop(box_1.index('game')), box_1.pop(box_1.index('watch'))])

# Swap the doll in Box 7 with the grass in Box 2
box_2[box_2.index('grass')], box_7[box_7.index('doll')] = box_7[box_7.index('doll')], box_2[box_2.index('grass')]

# Swap the jungle in Box 7 with the tree in Box 3
box_3[box_3.index('tree')], box_7[box_7.index('jungle')] = box_7[box_7.index('jungle')], box_3[box_3.index('tree')]

# Move the sun and the toy from Box 2 to Box 0
box_0.extend([box_2.pop(box_2.index('sun')), box_2.pop(box_2.index('toy'))])

# Move the rocket and the earring and the glasses from Box 1 to Box 3
box_3.extend([box_1.pop(box_1.index('rocket')), box_1.pop(box_1.index('earring')), box_1.pop(box_1.index('glasses'))])

# Move the doll from Box 2 to Box 4
box_4.append(box_2.pop(box_2.index('doll')))

# Replace the watch with the coat in Box 6
box_6[box_6.index('watch')] = 'coat'

# Remove the seaweed and the grass and the beach from Box 7
box_7.remove('seaweed')
box_7.remove('grass')
box_7.remove('beach')

# Replace the tree with the camera in Box 7
box_7[box_7.index('tree')] = 'camera'

# Put the fish into Box 9
box_9.append('fish')

# Remove the coat from Box 6
box_6.remove('coat')

# Swap the truck in Box 0 with the fish in Box 9
box_0[box_0.index('truck')], box_9[box_9.index('fish')] = box_9[box_9.index('fish')], box_0[box_0.index('truck')]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)
print("Box 9:", box_9)