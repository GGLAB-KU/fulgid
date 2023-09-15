box_0 = ['cow']
box_1 = ['watch', 'bus', 'lipstick', 'truck', 'jacket']
box_2 = ['soap']
box_3 = ['console', 'pants', 'train', 'bell']
box_4 = ['blender']

# Put the glove and the controller and the umbrella into Box 0
box_0.extend(['glove', 'controller', 'umbrella'])

# Empty Box 4
box_4 = []

# Move the umbrella from Box 0 to Box 2
box_2.append(box_0.pop(box_0.index('umbrella')))

# Move the lipstick and the bus and the truck from Box 1 to Box 3
box_3.extend([box_1.pop(box_1.index('lipstick')), box_1.pop(box_1.index('bus')), box_1.pop(box_1.index('truck'))])

# Replace the soap and the umbrella with the towel and the puzzle in Box 2
box_2 = ['towel', 'puzzle']

# Swap the jacket in Box 1 with the puzzle in Box 2
box_1[box_1.index('jacket')], box_2[box_2.index('puzzle')] = box_2[box_2.index('puzzle')], box_1[box_1.index('jacket')]

# Put the coin and the mask into Box 4
box_4.extend(['coin', 'mask'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)