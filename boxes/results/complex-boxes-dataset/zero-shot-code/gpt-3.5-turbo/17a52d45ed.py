box_0 = ['guitar', 'rock']
box_1 = ['basket', 'vase', 'speaker', 'coral']
box_2 = ['branch', 'scarf', 'freezer', 'rain', 'toothpaste']
box_3 = []

# Move the freezer from Box 2 to Box 3
box_3.append(box_2.pop(box_2.index('freezer')))

# Swap the freezer in Box 3 with the guitar in Box 0
box_0[box_0.index('guitar')], box_3[0] = box_3[0], box_0[box_0.index('guitar')]

# Replace the speaker and the basket and the coral with the shirt and the wire and the bracelet in Box 1
box_1[box_1.index('speaker')] = 'shirt'
box_1[box_1.index('basket')] = 'wire'
box_1[box_1.index('coral')] = 'bracelet'

# Put the harmonica and the sandals and the pan into Box 2
box_2.extend(['harmonica', 'sandals', 'pan'])

# Replace the freezer and the rock with the candle and the boot in Box 0
box_0[box_0.index('freezer')] = 'candle'
box_0[box_0.index('rock')] = 'boot'

# Move the pan and the scarf and the branch from Box 2 to Box 0
box_0.extend([box_2.pop(box_2.index('pan')), box_2.pop(box_2.index('scarf')), box_2.pop(box_2.index('branch'))])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)