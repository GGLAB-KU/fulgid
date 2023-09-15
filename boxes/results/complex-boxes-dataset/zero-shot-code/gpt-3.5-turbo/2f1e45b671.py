box_0 = ['meteor', 'bicycle', 'ocean']
box_1 = ['octopus', 'lamp', 'cat', 'button', 'dress']
box_2 = ['plate']
box_3 = ['violin']
box_4 = []
box_5 = ['grass']
box_6 = ['branch', 'mountain', 'dice']

# Put the horse into Box 6
box_6.append('horse')

# Replace the plate with the swimsuit in Box 2
box_2[0] = 'swimsuit'

# Move the branch and the horse from Box 6 to Box 4
box_4.extend([box_6.pop(0), box_6.pop(1)])

# Put the perfume and the mixer into Box 4
box_4.extend(['perfume', 'mixer'])

# Swap the violin in Box 3 with the cat in Box 1
box_3[0], box_1[box_1.index('cat')] = box_1[box_1.index('cat')], box_3[0]

# Move the mountain from Box 6 to Box 1
box_1.append(box_6.pop(1))

# Swap the lamp in Box 1 with the grass in Box 5
box_1[box_1.index('lamp')], box_5[0] = box_5[0], box_1[box_1.index('lamp')]

# Move the lamp from Box 5 to Box 3
box_3.append(box_5.pop(0))

# Swap the lamp in Box 3 with the meteor in Box 0
box_3[box_3.index('lamp')], box_0[box_0.index('meteor')] = box_0[box_0.index('meteor')], box_3[box_3.index('lamp')]

# Replace the dice with the toy in Box 6
box_6[box_6.index('dice')] = 'toy'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)