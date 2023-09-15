box_0 = ['wallet', 'snow', 'toothpaste', 'plane', 'pot']
box_1 = ['forest', 'wig', 'earring']
box_2 = ['freezer', 'oven']
box_3 = []
box_4 = ['shoes', 'meteor', 'game', 'zipper', 'moon']
box_5 = ['boot', 'bird', 'desert', 'mask', 'candle']
box_6 = ['key', 'needle', 'glasses']
box_7 = ['jacket', 'speaker']

# Swap bird in Box 5 with game in Box 4
box_4[2], box_5[1] = box_5[1], box_4[2]

# Replace mask with wire in Box 5
box_5[3] = 'wire'

# Replace oven and freezer with ocean and thunder in Box 2
box_2 = ['ocean', 'thunder']

# Move snow, toothpaste, and pot from Box 0 to Box 5
box_5.extend(box_0[1:4])
box_0[1:4] = []

# Put scissors, plate, and table into Box 7
box_7.extend(['scissors', 'plate', 'table'])

# Replace meteor, shoes, and zipper with charger, pillow, and piano in Box 4
box_4 = ['charger', 'pillow', 'piano']

# Empty Box 1
box_1 = []

# Put octopus into Box 7
box_7.append('octopus')

# Move needle, key, and glasses from Box 6 to Box 1
box_1.extend(box_6[0:3])
box_6[0:3] = []

# Swap moon in Box 4 with speaker in Box 7
box_4[4], box_7[1] = box_7[1], box_4[4]

# Move needle, glasses, and key from Box 1 to Box 0
box_0.extend(box_1[0:3])
box_1[0:3] = []

# Remove wire from Box 5
box_5.remove('wire')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)