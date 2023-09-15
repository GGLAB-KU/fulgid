box_0 = ['skirt', 'toaster', 'telescope']
box_1 = ['horse', 'umbrella', 'bicycle']
box_2 = ['lion', 'puzzle', 'lightning', 'swimsuit']
box_3 = ['watch', 'candle']
box_4 = ['jacket', 'helmet', 'motorcycle', 'pants', 'bell']

# Swap swimsuit with telescope
box_0[2], box_2[3] = box_2[3], box_0[2]

# Swap watch with bicycle
box_1[2], box_3[0] = box_3[0], box_1[2]

# Replace bicycle with boot
box_3[0] = 'boot'

# Put grinder and glove into Box 3
box_3.extend(['grinder', 'glove'])

# Replace grinder, boot, and candle with laptop, earring, and makeup
box_3[0:3] = ['laptop', 'earring', 'makeup']

# Put table into Box 3
box_3.append('table')

# Move umbrella from Box 1 to Box 4
box_4.append(box_1.pop(1))

# Swap makeup with skirt
box_0[0], box_3[2] = box_3[2], box_0[0]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)