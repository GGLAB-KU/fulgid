box_0 = ['wire', 'submarine', 'ship']
box_1 = ['forest', 'dress']
box_2 = ['comb', 'bowl', 'octopus']
box_3 = ['coat', 'ocean', 'candle', 'bracelet']
box_4 = ['shoe', 'boat', 'clock', 'toothbrush']
box_5 = ['microwave', 'polish', 'needle', 'razor', 'bag']

# Replace items in Box 3
box_3[1] = 'grinder'
box_3[3] = 'cat'
box_3.append('paint')

# Swap toothbrush in Box 4 with bowl in Box 2
box_4[3], box_2[1] = box_2[1], box_4[3]

# Remove items from Box 2
box_2.remove('comb')
box_2.remove('octopus')
box_2.remove('toothbrush')

# Put items into Box 5
box_5.extend(['octopus', 'bell', 'vase'])

# Put forest and card into Box 4
box_4.append('forest')
box_4.append('card')

# Swap razor in Box 5 with cat in Box 3
box_5[3], box_3[1] = box_3[1], box_5[3]

# Replace wire with scissors in Box 0
box_0[0] = 'scissors'

# Put comb into Box 0
box_0.append('comb')

# Move cat from Box 5 to Box 3
box_3.append(box_5.pop(3))

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)