box_0 = []
box_1 = ['camera', 'boat', 'jacket']
box_2 = ['bowl', 'snow', 'plane', 'bag']
box_3 = ['microscope']

# Put the rock and the tiger into Box 1
box_1.append('rock')
box_1.append('tiger')

# Move the microscope from Box 3 to Box 1
box_1.append(box_3.pop())

# Put the glasses and the basket and the sock into Box 1
box_1.extend(['glasses', 'basket', 'sock'])

# Put the puzzle and the pan and the toy into Box 2
box_2.extend(['puzzle', 'pan', 'toy'])

# Swap the pan in Box 2 with the tiger in Box 1
box_1[box_1.index('tiger')], box_2[box_2.index('pan')] = box_2[box_2.index('pan')], box_1[box_1.index('tiger')]

# Put the apple into Box 3
box_3.append('apple')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)