box_0 = ['dice', 'horn', 'elephant', 'wallet', 'coin']
box_1 = ['pen', 'octopus', 'brush', 'thunder']
box_2 = ['lightning', 'doll', 'toy', 'shampoo', 'mixer']
box_3 = ['grass']
box_4 = ['toothpaste']
box_5 = ['forest', 'star', 'clock', 'spoon', 'lock']

# Swap the lock in Box 5 with the octopus in Box 1
box_1[box_1.index('octopus')], box_5[box_5.index('lock')] = box_5[box_5.index('lock')], box_1[box_1.index('octopus')]

# Replace the toothpaste with the telescope in Box 4
box_4[box_4.index('toothpaste')] = 'telescope'

# Swap the toy in Box 2 with the grass in Box 3
box_2[box_2.index('toy')], box_3[box_3.index('grass')] = box_3[box_3.index('grass')], box_2[box_2.index('toy')]

# Remove the shampoo and the doll from Box 2
box_2.remove('shampoo')
box_2.remove('doll')

# Remove the dice and the horn and the coin from Box 0
box_0.remove('dice')
box_0.remove('horn')
box_0.remove('coin')

# Replace the forest with the beach in Box 5
box_5[box_5.index('forest')] = 'beach'

# Move the telescope from Box 4 to Box 0
box_0.append(box_4.pop(box_4.index('telescope')))

# Swap the lightning in Box 2 with the elephant in Box 0
box_0[box_0.index('elephant')], box_2[box_2.index('lightning')] = box_2[box_2.index('lightning')], box_0[box_0.index('elephant')]

# Remove the star from Box 5
box_5.remove('star')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)