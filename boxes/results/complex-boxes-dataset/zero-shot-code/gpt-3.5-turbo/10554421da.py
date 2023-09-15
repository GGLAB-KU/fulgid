box0 = ['earring', 'lion', 'polish', 'vase']
box1 = ['bear', 'starfish', 'bell']
box2 = ['bag']
box3 = ['thread']
box4 = ['elephant', 'plane', 'microscope', 'lipstick']

# Move items from Box 4 to Box 0
box0.extend(box4)
box4.clear()

# Move thread from Box 3 to Box 1
box1.append(box3.pop())

# Move items from Box 0 to Box 1
box1.extend([box0.pop(box0.index('microscope')), box0.pop(box0.index('earring')), box0.pop(box0.index('vase'))])

# Remove bear from Box 1
box1.remove('bear')

# Put snow into Box 0
box0.append('snow')

# Remove items from Box 1
box1.remove('microscope')
box1.remove('earring')
box1.remove('bell')

# Swap lipstick in Box 4 with lion in Box 0
box0[box0.index('lion')], box4[box4.index('lipstick')] = box4[box4.index('lipstick')], box0[box0.index('lion')]

# Print the final state of the boxes
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)