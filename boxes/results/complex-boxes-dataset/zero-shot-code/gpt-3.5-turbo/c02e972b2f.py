box_0 = ['crown', 'phone', 'frame']
box_1 = ['watch', 'needle', 'polish']
box_2 = ['pants', 'shelf']
box_3 = ['ocean']
box_4 = ['comet']
box_5 = []
box_6 = ['scissors']
box_7 = ['belt', 'note', 'sun', 'spoon', 'fork']
box_8 = ['pot', 'butterfly', 'fridge', 'chair', 'motorcycle']

# Swap needle in Box 1 with crown in Box 0
box_0[0], box_1[1] = box_1[1], box_0[0]

# Put skirt, jacket, and microwave into Box 2
box_2.extend(['skirt', 'jacket', 'microwave'])

# Move ocean from Box 3 to Box 6
box_6.append(box_3.pop(0))

# Put pen and guitar into Box 1
box_1.extend(['pen', 'guitar'])

# Remove belt, fork, and spoon from Box 7
box_7.remove('belt')
box_7.remove('fork')
box_7.remove('spoon')

# Put paint, violin, and boat into Box 3
box_3.extend(['paint', 'violin', 'boat'])

# Move violin and paint from Box 3 to Box 4
box_4.extend([box_3.pop(1), box_3.pop(1)])

# Remove guitar, watch, and pen from Box 1
box_1.remove('guitar')
box_1.remove('watch')
box_1.remove('pen')

# Replace crown and polish with perfume and violin in Box 1
box_1[0] = 'perfume'
box_1.append('violin')

# Remove violin and perfume from Box 1
box_1.remove('violin')
box_1.remove('perfume')

# Replace microwave, jacket, and pants with glasses, snow, and pillow in Box 2
box_2 = ['glasses', 'snow', 'pillow']

# Put necklace, beach, and card into Box 7
box_7.extend(['necklace', 'beach', 'card'])

# Remove violin, comet, and paint from Box 4
box_4.remove('violin')
box_4.remove('comet')
box_4.remove('paint')

# Move pillow, snow, and glasses from Box 2 to Box 3
box_3.extend([box_2.pop(2), box_2.pop(1), box_2.pop(0)])

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