box_0 = ['sock', 'controller', 'wig']
box_1 = ['star', 'blender', 'drum']
box_2 = []
box_3 = ['chair', 'book', 'perfume', 'bell']
box_4 = ['grass']
box_5 = ['pillow']
box_6 = ['shampoo', 'branch']
box_7 = ['bird', 'tree']
box_8 = ['freezer', 'mixer']
box_9 = ['pants', 'river', 'tiger']
box_10 = ['shoe']

# Move the tiger from Box 9 to Box 5
box_5.append(box_9.pop(box_9.index('tiger')))

# Put the bowl and the violin and the submarine into Box 6
box_6.extend(['bowl', 'violin', 'submarine'])

# Put the fish and the console and the shampoo into Box 9
box_9.extend(['fish', 'console', 'shampoo'])

# Replace the tree with the soap in Box 7
box_7[box_7.index('tree')] = 'soap'

# Remove the mixer from Box 8
box_8.remove('mixer')

# Put the shoe and the dolphin and the freezer into Box 1
box_1.extend(['shoe', 'dolphin', 'freezer'])

# Replace the shoe with the battery in Box 10
box_10[box_10.index('shoe')] = 'battery'

# Swap the soap in Box 7 with the book in Box 3
box_7[box_7.index('soap')], box_3[box_3.index('book')] = box_3[box_3.index('book')], box_7[box_7.index('soap')]

# Swap the shampoo in Box 6 with the bird in Box 7
box_6[box_6.index('shampoo')], box_7[box_7.index('bird')] = box_7[box_7.index('bird')], box_6[box_6.index('shampoo')]

# Move the bell and the perfume and the soap from Box 3 to Box 6
box_6.extend([box_3.pop(box_3.index('bell')), box_3.pop(box_3.index('perfume')), box_3.pop(box_3.index('soap'))])

# Replace the shampoo with the lock in Box 7
box_7[box_7.index('shampoo')] = 'lock'

# Remove the sock and the controller from Box 0
box_0.remove('sock')
box_0.remove('controller')

# Move the freezer from Box 8 to Box 1
box_1.append(box_8.pop(box_8.index('freezer')))

# Move the chair from Box 3 to Box 5
box_5.append(box_3.pop(box_3.index('chair')))

# Remove the battery from Box 10
box_10.remove('battery')

# Swap the chair in Box 5 with the wig in Box 0
box_5[box_5.index('chair')], box_0[box_0.index('wig')] = box_0[box_0.index('wig')], box_5[box_5.index('chair')]

# Replace the tiger and the pillow and the wig with the cow and the cloud and the bicycle in Box 5
box_5[box_5.index('tiger')] = 'cow'
box_5[box_5.index('pillow')] = 'cloud'
box_5[box_5.index('wig')] = 'bicycle'

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