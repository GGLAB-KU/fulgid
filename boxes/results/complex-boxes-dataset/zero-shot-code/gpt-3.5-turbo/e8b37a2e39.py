box_0 = ['keyboard', 'flower']
box_1 = ['belt', 'apple', 'battery', 'forest']
box_2 = []
box_3 = []
box_4 = ['earring', 'horn', 'mask', 'note']
box_5 = ['harmonica', 'microscope', 'blender']
box_6 = ['dice', 'submarine', 'card', 'snow']
box_7 = ['mixer', 'laptop']

# Move the keyboard from Box 0 to Box 7
box_7.append(box_0.pop(0))

# Swap the forest in Box 1 with the flower in Box 0
box_0[0], box_1[3] = box_1[3], box_0[0]

# Remove the horn and the mask from Box 4
box_4.remove('horn')
box_4.remove('mask')

# Remove the blender and the microscope and the harmonica from Box 5
box_5.remove('blender')
box_5.remove('microscope')
box_5.remove('harmonica')

# Replace the apple with the desert in Box 1
box_1[1] = 'desert'

# Move the snow and the dice and the submarine from Box 6 to Box 2
box_2.extend(box_6[3:])
box_6[3:] = []

# Remove the earring and the note from Box 4
box_4.remove('earring')
box_4.remove('note')

# Remove the card from Box 6
box_6.remove('card')

# Move the snow and the dice and the submarine from Box 2 to Box 5
box_5.extend(box_2)
box_2 = []

# Put the ocean and the elephant and the wig into Box 2
box_2.extend(['ocean', 'elephant', 'wig'])

# Remove the dice and the submarine and the snow from Box 5
box_5.remove('dice')
box_5.remove('submarine')
box_5.remove('snow')

# Remove the belt and the desert and the battery from Box 1
box_1.remove('belt')
box_1.remove('desert')
box_1.remove('battery')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)