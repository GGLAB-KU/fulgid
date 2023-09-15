box_0 = ['coat']
box_1 = ['microscope', 'candle', 'tree', 'pillow', 'guitar']
box_2 = ['horse', 'shark', 'magnet', 'mirror']
box_3 = ['lipstick', 'star']
box_4 = []
box_5 = ['earring']
box_6 = ['headphone', 'comet', 'polish', 'speaker', 'dog']

# Replace the coat with the plane in Box 0
box_0 = ['plane']

# Replace the comet and the dog with the storm and the meteor in Box 6
box_6 = ['storm', 'meteor']

# Move the headphone from Box 6 to Box 1
box_1.append(box_6.pop(0))

# Empty Box 3
box_3 = []

# Put the pen into Box 0
box_0.append('pen')

# Swap the guitar in Box 1 with the plane in Box 0
box_0, box_1 = box_1, box_0

# Move the storm and the meteor and the speaker from Box 6 to Box 2
box_2.extend(box_6)
box_6 = []

# Swap the pen in Box 0 with the earring in Box 5
box_0[1], box_5[0] = box_5[0], box_0[1]

# Move the guitar from Box 0 to Box 2
box_2.append(box_0.pop(1))

# Put the toothpaste and the mirror and the pants into Box 1
box_1.extend(['toothpaste', 'mirror', 'pants'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)