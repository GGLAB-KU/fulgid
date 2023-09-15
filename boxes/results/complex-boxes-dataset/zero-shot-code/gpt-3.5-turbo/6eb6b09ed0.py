box_0 = ['zipper']
box_1 = ['hat', 'needle']
box_2 = ['towel', 'plate']
box_3 = []
box_4 = ['button', 'storm', 'card']

# Replace the zipper with the belt in Box 0
box_0 = ['belt']

# Move the needle from Box 1 to Box 3
box_3.append(box_1.pop(box_1.index('needle')))

# Put the keyboard into Box 4
box_4.append('keyboard')

# Put the shampoo and the bicycle and the pants into Box 3
box_3.extend(['shampoo', 'bicycle', 'pants'])

# Replace the card and the storm with the rock and the octopus in Box 4
box_4.remove('card')
box_4.remove('storm')
box_4.extend(['rock', 'octopus'])

# Swap the towel in Box 2 with the hat in Box 1
box_1[box_1.index('hat')], box_2[box_2.index('towel')] = box_2[box_2.index('towel')], box_1[box_1.index('hat')]

# Remove the belt from Box 0
box_0 = []

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)