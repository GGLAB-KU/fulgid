box_0 = ['rain', 'controller', 'necklace', 'flute']
box_1 = ['grass', 'oven']
box_2 = ['keyboard', 'book']
box_3 = ['thunder', 'train', 'frame', 'fork']
box_4 = ['microscope', 'mirror', 'boot', 'charger', 'wallet']
box_5 = ['shark', 'earring', 'piano', 'tiger']
box_6 = ['pan', 'submarine', 'towel', 'harmonica', 'shirt']
box_7 = []
box_8 = ['bowl', 'cloud', 'toy', 'telescope']
box_9 = ['apple']
box_10 = ['camera', 'belt', 'coat', 'shoes']
box_11 = ['mask', 'speaker', 'river']
box_12 = ['note', 'candle']

# Put the key and the button and the crown into Box 12
box_12.extend(['key', 'button', 'crown'])

# Swap the apple in Box 9 with the book in Box 2
box_9[0], box_2[1] = box_2[1], box_9[0]

# Put the coin and the oven into Box 1
box_1.extend(['coin', 'oven'])

# Replace the telescope and the bowl and the toy with the apple and the chair and the toaster in Box 8
box_8 = ['apple', 'chair', 'toaster']

# Swap the apple in Box 8 with the thunder in Box 3
box_8[0], box_3[0] = box_3[0], box_8[0]

# Remove the speaker and the mask and the river from Box 11
box_11 = []

# Move the oven from Box 1 to Box 0
box_0.append(box_1.pop(box_1.index('oven')))

# Replace the ocean and the grass and the coin with the controller and the needle and the mixer in Box 1
box_1 = ['controller', 'needle', 'mixer']

# Remove the piano and the tiger from Box 5
box_5.remove('piano')
box_5.remove('tiger')

# Replace the boot and the microscope with the dress and the bear in Box 4
box_4 = ['dress', 'bear']

# Remove the dress from Box 4
box_4.remove('dress')

# Remove the pan from Box 6
box_6.remove('pan')

# Remove the cloud and the toaster from Box 8
box_8.remove('cloud')
box_8.remove('toaster')

# Put the blanket and the sculpture into Box 8
box_8.extend(['blanket', 'sculpture'])

# Remove the shark and the earring from Box 5
box_5.remove('shark')
box_5.remove('earring')

# Remove the frame from Box 3
box_3.remove('frame')

# Move the keyboard and the apple from Box 2 to Box 0
box_0.extend([box_2.pop(0), box_2.pop(0)])

# Swap the button in Box 12 with the book in Box 9
box_12[1], box_9[0] = box_9[0], box_12[1]

# Move the belt from Box 10 to Box 7
box_7.append(box_10.pop(box_10.index('belt')))

# Put the soap into Box 1
box_1.append('soap')

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