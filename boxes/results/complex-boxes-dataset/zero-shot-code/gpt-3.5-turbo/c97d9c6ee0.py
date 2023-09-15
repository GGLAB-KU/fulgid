box_0 = ['gloves', 'horse', 'pen', 'fish']
box_1 = ['candle', 'speaker']
box_2 = ['dice']
box_3 = ['pillow', 'lightning']
box_4 = ['blanket', 'vase', 'basket', 'jacket']
box_5 = []
box_6 = ['cup', 'pot', 'thread', 'needle']

# Move the thread from Box 6 to Box 1
box_1.append(box_6.pop(box_6.index('thread')))

# Move the candle and the speaker from Box 1 to Box 4
box_4.extend([box_1.pop(box_1.index('candle')), box_1.pop(box_1.index('speaker'))])

# Remove the pillow from Box 3
box_3.remove('pillow')

# Swap the dice in Box 2 with the lightning in Box 3
box_2[0], box_3[box_3.index('lightning')] = box_3[box_3.index('lightning')], box_2[0]

# Replace the dice with the ship in Box 3
box_3[box_3.index('lightning')] = 'ship'

# Swap the ship in Box 3 with the pot in Box 6
box_3[box_3.index('ship')], box_6[box_6.index('pot')] = box_6[box_6.index('pot')], box_3[box_3.index('ship')]

# Remove the lightning from Box 2
box_2.remove('lightning')

# Put the blanket and the skirt and the cloud into Box 5
box_5.extend(['blanket', 'skirt', 'cloud'])

# Replace the fish with the scarf in Box 0
box_0[box_0.index('fish')] = 'scarf'

# Remove the cloud from Box 5
box_5.remove('cloud')

# Replace the thread with the sandals in Box 1
box_1[box_1.index('thread')] = 'sandals'

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)