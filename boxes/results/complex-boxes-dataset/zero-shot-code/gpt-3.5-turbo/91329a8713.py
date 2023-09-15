box_0 = ['elephant']
box_1 = ['hat']
box_2 = ['controller', 'sun', 'ring', 'candle']
box_3 = ['perfume', 'usb', 'freezer']
box_4 = ['lipstick', 'mask', 'sandals']
box_5 = []
box_6 = ['seaweed', 'forest', 'plate', 'telescope']

# Remove lipstick and mask from Box 4
box_4.remove('lipstick')
box_4.remove('mask')

# Remove perfume and usb from Box 3
box_3.remove('perfume')
box_3.remove('usb')

# Swap sandals in Box 4 with forest in Box 6
box_4.remove('sandals')
box_6.remove('forest')
box_4.append('forest')
box_6.append('sandals')

# Move elephant from Box 0 to Box 2
box_0.remove('elephant')
box_2.append('elephant')

# Remove forest from Box 4
box_4.remove('forest')

# Remove hat from Box 1
box_1.remove('hat')

# Replace sun and controller with basket and snow in Box 2
box_2.remove('controller')
box_2.remove('sun')
box_2.append('basket')
box_2.append('snow')

# Empty Box 6
box_6 = []

# Put note into Box 2
box_2.append('note')

# Empty Box 3
box_3 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)