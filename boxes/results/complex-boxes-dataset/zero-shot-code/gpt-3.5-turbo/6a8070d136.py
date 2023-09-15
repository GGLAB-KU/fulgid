box_0 = ['branch']
box_1 = ['car', 'console', 'shoe', 'pillow']
box_2 = ['needle', 'sock', 'desert']
box_3 = ['snow', 'flower', 'elephant', 'note']
box_4 = ['meteor', 'earring']
box_5 = []
box_6 = ['shampoo', 'candle', 'toaster', 'beach', 'flute']
box_7 = ['basket', 'toothbrush']
box_8 = ['lion']
box_9 = []
box_10 = ['bowl', 'shelf', 'razor', 'puzzle']
box_11 = ['bus', 'oven']
box_12 = ['coral', 'boat', 'chair']
box_13 = ['glove']

# Swap the desert in Box 2 with the coral in Box 12
box_2[2], box_12[0] = box_12[0], box_2[2]

# Put the sock and the snow and the motorcycle into Box 6
box_6.extend(['sock', 'snow', 'motorcycle'])

# Empty Box 2
box_2 = []

# Move the earring from Box 4 to Box 12
box_12.append(box_4.pop())

# Put the jungle into Box 11
box_11.append('jungle')

# Remove the bus and the jungle from Box 11
box_11.remove('bus')
box_11.remove('jungle')

# Swap the oven in Box 11 with the branch in Box 0
box_0[0], box_11[1] = box_11[1], box_0[0]

# Empty Box 8
box_8 = []

# Put the violin and the headphone and the sock into Box 7
box_7.extend(['violin', 'headphone', 'sock'])

# Move the meteor from Box 4 to Box 2
box_2.append(box_4.pop())

# Move the meteor from Box 2 to Box 12
box_12.append(box_2.pop())

# Remove the toaster from Box 6
box_6.remove('toaster')

# Swap the branch in Box 11 with the razor in Box 10
box_10[2], box_11[0] = box_11[0], box_10[2]

# Move the boat and the chair and the desert from Box 12 to Box 13
box_13.extend([box_12.pop(1), box_12.pop(1), box_12.pop()])

# Put the chair and the sock into Box 4
box_4.extend(['chair', 'sock'])

# Move the shoe and the console from Box 1 to Box 3
box_3.extend([box_1.pop(2), box_1.pop(1)])

# Move the meteor from Box 12 to Box 7
box_7.append(box_12.pop())

# Swap the glove in Box 13 with the razor in Box 11
box_11[2], box_13[0] = box_13[0], box_11[2]

# Swap the car in Box 1 with the razor in Box 13
box_1[0], box_13[1] = box_13[1], box_1[0]

# Put the grass and the soap into Box 1
box_1.extend(['grass', 'soap'])

# Put the dolphin into Box 8
box_8.append('dolphin')

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
print("Box 10:", box_10)
print("Box 11:", box_11)
print("Box 12:", box_12)
print("Box 13:", box_13)