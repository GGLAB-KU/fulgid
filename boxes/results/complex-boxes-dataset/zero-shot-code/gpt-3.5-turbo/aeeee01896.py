box_0 = ['violin', 'lightning', 'battery']
box_1 = []
box_2 = ['coin', 'blender', 'island']
box_3 = ['basket', 'bear', 'motorcycle', 'leaf', 'tie']
box_4 = ['car', 'charger', 'sun', 'belt', 'candle']
box_5 = ['comet', 'octopus', 'bus', 'phone']
box_6 = ['coral', 'shampoo', 'needle', 'planet']
box_7 = []
box_8 = []
box_9 = ['whistle', 'rocket', 'lipstick', 'microscope']
box_10 = ['storm']
box_11 = ['polish']
box_12 = ['guitar', 'watch', 'scarf']
box_13 = ['keyboard']

# Remove whistle, rocket, and microscope from Box 9
box_9.remove('whistle')
box_9.remove('rocket')
box_9.remove('microscope')

# Move storm from Box 10 to Box 12
box_12.append(box_10.pop())

# Remove leaf from Box 3
box_3.remove('leaf')

# Swap polish in Box 11 with planet in Box 6
box_11[0], box_6[3] = box_6[3], box_11[0]

# Move storm, scarf, and watch from Box 12 to Box 4
box_4.extend([box_12.pop(), box_12.pop(), box_12.pop()])

# Replace keyboard with harmonica in Box 13
box_13[0] = 'harmonica'

# Put boot into Box 0
box_0.append('boot')

# Put swimsuit and perfume into Box 6
box_6.extend(['swimsuit', 'perfume'])

# Swap lightning in Box 0 with guitar in Box 12
box_0[0], box_12[0] = box_12[0], box_0[0]

# Swap lipstick in Box 9 with tie in Box 3
box_9[1], box_3[4] = box_3[4], box_9[1]

# Empty Box 9
box_9.clear()

# Swap polish in Box 6 with belt in Box 4
box_6[1], box_4[3] = box_4[3], box_6[1]

# Swap swimsuit in Box 6 with bus in Box 5
box_6[2], box_5[2] = box_5[2], box_6[2]

# Remove octopus from Box 5
box_5.remove('octopus')

# Move planet from Box 11 to Box 8
box_8.append(box_11.pop())

# Replace island with mask in Box 2
box_2[2] = 'mask'

# Swap needle in Box 6 with motorcycle in Box 3
box_6[2], box_3[2] = box_3[2], box_6[2]

# Put glasses into Box 9
box_9.append('glasses')

# Swap boot in Box 0 with planet in Box 8
box_0[1], box_8[0] = box_8[0], box_0[1]

# Replace mask with tie in Box 2
box_2[2] = 'tie'

# Swap blender in Box 2 with phone in Box 5
box_2[1], box_5[3] = box_5[3], box_2[1]

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