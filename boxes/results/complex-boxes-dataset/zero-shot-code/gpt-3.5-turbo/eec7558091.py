box_0 = ['scissors']
box_1 = ['mask']
box_2 = ['car', 'violin']
box_3 = ['razor', 'mirror']
box_4 = []
box_5 = ['coin', 'clock', 'console', 'perfume', 'whistle']
box_6 = ['paint']
box_7 = []
box_8 = ['headphone']

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)

# Move the paint from Box 6 to Box 1
box_1.append(box_6.pop(0))

# Swap the mask in Box 1 with the scissors in Box 0
box_0[0], box_1[0] = box_1[0], box_0[0]

# Put the branch and the forest and the card into Box 3
box_3.extend(['branch', 'forest', 'card'])

# Put the shirt into Box 4
box_4.append('shirt')

# Remove the console and the perfume and the coin from Box 5
box_5.remove('console')
box_5.remove('perfume')
box_5.remove('coin')

# Move the mask from Box 0 to Box 3
box_3.append(box_0.pop(0))

# Put the dog and the sandals and the thunder into Box 7
box_7.extend(['dog', 'sandals', 'thunder'])

# Replace the paint and the scissors with the piano and the mixer in Box 1
box_1 = ['piano', 'mixer']

# Put the coin and the charger into Box 3
box_3.extend(['coin', 'charger'])

# Move the piano and the mixer from Box 1 to Box 3
box_3.extend(box_1)
box_1 = []

# Swap the car in Box 2 with the whistle in Box 5
box_2[0], box_5[3] = box_5[3], box_2[0]

# Swap the piano in Box 3 with the headphone in Box 8
box_3[0], box_8[0] = box_8[0], box_3[0]

# Put the lamp and the skirt and the dog into Box 7
box_7.extend(['lamp', 'skirt', 'dog'])

# Remove the clock and the car from Box 5
box_5.remove('clock')
box_5.remove('car')

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)