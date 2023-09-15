box_0 = ['dog', 'blender', 'mountain']
box_1 = []
box_2 = ['pen', 'ship', 'shoes', 'pants']
box_3 = ['lamp', 'book', 'brush', 'microscope']
box_4 = []
box_5 = ['submarine', 'snow']
box_6 = ['phone', 'lipstick']

# Put the clock and the pen into Box 2
box_2.append('clock')
box_2.append('pen')

# Replace the blender and the mountain with the mirror and the storm in Box 0
box_0.remove('blender')
box_0.remove('mountain')
box_0.append('mirror')
box_0.append('storm')

# Swap the mirror in Box 0 with the ship in Box 2
box_0.remove('mirror')
box_2.remove('ship')
box_0.append('ship')
box_2.append('mirror')

# Replace the dog and the ship and the storm with the razor and the plate and the horse in Box 0
box_0.remove('dog')
box_0.remove('ship')
box_0.remove('storm')
box_0.append('razor')
box_0.append('plate')
box_0.append('horse')

# Put the phone into Box 3
box_3.append('phone')

# Swap the pants in Box 2 with the lamp in Box 3
box_2.remove('pants')
box_3.remove('lamp')
box_2.append('lamp')
box_3.append('pants')

# Swap the snow in Box 5 with the mirror in Box 2
box_5.remove('snow')
box_2.remove('mirror')
box_5.append('mirror')
box_2.append('snow')

# Remove the lipstick from Box 6
box_6.remove('lipstick')

# Remove the phone from Box 6
box_6.remove('phone')

# Empty Box 0
box_0 = []

# Move the mirror and the submarine from Box 5 to Box 3
box_5.remove('mirror')
box_3.append('mirror')
box_5.remove('submarine')
box_3.append('submarine')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)