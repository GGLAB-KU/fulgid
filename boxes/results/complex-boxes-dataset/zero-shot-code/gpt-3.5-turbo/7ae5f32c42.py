box_0 = ['headphone', 'planet', 'shampoo', 'shorts']
box_1 = ['cup', 'magnet', 'game', 'note']
box_2 = ['key', 'thunder']
box_3 = ['pillow', 'needle', 'blanket', 'boat', 'mirror']
box_4 = ['horn', 'dolphin', 'freezer', 'towel']

# Put the violin and the bear into Box 0
box_0.extend(['violin', 'bear'])

# Swap the towel in Box 4 with the shampoo in Box 0
box_0[box_0.index('shampoo')], box_4[box_4.index('towel')] = box_4[box_4.index('towel')], box_0[box_0.index('shampoo')]

# Remove the blanket from Box 3
box_3.remove('blanket')

# Replace the magnet and the cup with the plate and the book in Box 1
box_1[box_1.index('magnet')] = 'plate'
box_1[box_1.index('cup')] = 'book'

# Swap the pillow in Box 3 with the book in Box 1
box_3[box_3.index('pillow')], box_1[box_1.index('book')] = box_1[box_1.index('book')], box_3[box_3.index('pillow')]

# Replace the headphone and the shorts and the violin with the drum and the ring and the telescope in Box 0
box_0[box_0.index('headphone')] = 'drum'
box_0[box_0.index('shorts')] = 'ring'
box_0[box_0.index('violin')] = 'telescope'

# Remove the telescope from Box 0
box_0.remove('telescope')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)