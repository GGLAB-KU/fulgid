box_0 = ['dolphin', 'brush', 'pillow', 'desert']
box_1 = []
box_2 = ['starfish', 'lion', 'table']
box_3 = []
box_4 = ['soap', 'thunder', 'storm', 'rain', 'lamp']
box_5 = ['shoes', 'cup', 'usb', 'planet', 'laptop']

# Move thunder and storm from Box 4 to Box 1
box_1.extend([box_4.pop(box_4.index('thunder')), box_4.pop(box_4.index('storm'))])

# Move soap and storm from Box 1 to Box 2
box_2.extend([box_1.pop(box_1.index('soap')), box_1.pop(box_1.index('storm'))])

# Remove lamp from Box 4
box_4.remove('lamp')

# Put microscope into Box 1
box_1.append('microscope')

# Put earring into Box 5
box_5.append('earring')

# Put bracelet into Box 0
box_0.append('bracelet')

# Swap lion in Box 2 with bracelet in Box 0
box_2[box_2.index('lion')], box_0[box_0.index('bracelet')] = box_0[box_0.index('bracelet')], box_2[box_2.index('lion')]

# Remove rain from Box 4
box_4.remove('rain')

# Remove microscope and thunder from Box 1
box_1.remove('microscope')
box_1.remove('thunder')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)