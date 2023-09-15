box_0 = ['blender']
box_1 = ['pan', 'flute']
box_2 = ['grinder', 'microscope', 'meteor', 'pants', 'doll']
box_3 = ['rock', 'ocean', 'mountain', 'candle']
box_4 = ['earring', 'clock', 'lock', 'sun']
box_5 = ['bowl']
box_6 = ['sculpture']

# Swap blender in Box 0 with grinder in Box 2
box_0[0], box_2[0] = box_2[0], box_0[0]

# Put blender and pan into Box 3
box_3.extend([box_0[0], box_1[0]])

# Remove pan and flute from Box 1
box_1.remove('pan')
box_1.remove('flute')

# Replace sculpture with gloves in Box 6
box_6[0] = 'gloves'

# Move pan from Box 3 to Box 0
box_0.append(box_3.pop(2))

# Remove earring from Box 4
box_4.remove('earring')

# Replace pants and blender with snow and horn in Box 2
box_2[3:5] = ['snow', 'horn']

# Replace rock, blender, and mountain with note, moon, and octopus in Box 3
box_3[0:3] = ['note', 'moon', 'octopus']

# Swap moon in Box 3 with gloves in Box 6
box_3[1], box_6[0] = box_6[0], box_3[1]

# Put flute, gloves, and ring into Box 3
box_3.extend([box_1[0], box_6[0], 'ring'])

# Remove snow from Box 2
box_2.remove('snow')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)