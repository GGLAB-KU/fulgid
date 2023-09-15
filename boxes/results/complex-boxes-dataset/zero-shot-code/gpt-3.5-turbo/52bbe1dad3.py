box_0 = ['fish', 'glove', 'boot', 'watch', 'shoes']
box_1 = ['sock', 'leaf']
box_2 = ['horn']
box_3 = ['truck', 'motorcycle', 'pen', 'fridge', 'drum']
box_4 = []
box_5 = ['microwave', 'coin']
box_6 = ['cup', 'makeup', 'lion', 'freezer', 'pants']
box_7 = ['fork']
box_8 = []
box_9 = []

# Move the glove from Box 0 to Box 3
box_3.append(box_0.pop(box_0.index('glove')))

# Remove the truck from Box 3
box_3.remove('truck')

# Swap the boot in Box 0 with the microwave in Box 5
box_0[box_0.index('boot')], box_5[box_5.index('microwave')] = box_5[box_5.index('microwave')], box_0[box_0.index('boot')]

# Replace the shoes with the scissors in Box 0
box_0[box_0.index('shoes')] = 'scissors'

# Swap the coin in Box 5 with the sock in Box 1
box_5[box_5.index('coin')], box_1[box_1.index('sock')] = box_1[box_1.index('sock')], box_5[box_5.index('coin')]

# Replace the fork with the sandals in Box 7
box_7[box_7.index('fork')] = 'sandals'

# Replace the scissors and the fish with the comet and the star in Box 0
box_0[box_0.index('scissors')] = 'comet'
box_0[box_0.index('fish')] = 'star'

# Replace the star and the microwave and the comet with the starfish and the shoes and the wallet in Box 0
box_0[box_0.index('star')] = 'starfish'
box_0[box_0.index('shoes')] = 'wallet'
box_0.remove('comet')

# Move the lion from Box 6 to Box 3
box_3.append(box_6.pop(box_6.index('lion')))

# Move the coin and the leaf from Box 1 to Box 2
box_2.extend([box_1.pop(box_1.index('coin')), box_1.pop(box_1.index('leaf'))])

# Remove the cup and the makeup from Box 6
box_6.remove('cup')
box_6.remove('makeup')

# Put the drum into Box 8
box_8.append(box_3.pop(box_3.index('drum')))

# Move the horn and the leaf and the coin from Box 2 to Box 7
box_7.extend([box_2.pop(box_2.index('horn')), box_2.pop(box_2.index('leaf')), box_2.pop(box_2.index('coin'))])

# Put the blender and the river and the pot into Box 9
box_9.extend(['blender', 'river', 'pot'])

# Remove the pants from Box 6
box_6.remove('pants')

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