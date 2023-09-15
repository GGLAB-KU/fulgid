box_0 = ['bear', 'thunder', 'blender', 'earring']
box_1 = ['towel', 'console']
box_2 = ['car', 'lamp']
box_3 = ['truck', 'spoon', 'pan', 'beach', 'comet']
box_4 = ['laptop', 'plate', 'skirt']
box_5 = []
box_6 = ['microscope', 'oven']

# Remove the comet, beach, and spoon from Box 3
box_3.remove('comet')
box_3.remove('beach')
box_3.remove('spoon')

# Put the keyboard into Box 0
box_0.append('keyboard')

# Move the console and towel from Box 1 to Box 3
box_3.extend(box_1)
box_1.clear()

# Move the oven and microscope from Box 6 to Box 2
box_2.extend(box_6)
box_6.clear()

# Put the wig, grinder, and bowl into Box 4
box_4.extend(['wig', 'grinder', 'bowl'])

# Swap the lamp in Box 2 with the laptop in Box 4
box_2[1], box_4[0] = box_4[0], box_2[1]

# Move the microscope from Box 2 to Box 0
box_0.append(box_2.pop(1))

# Empty Box 4
box_4.clear()

# Swap the car in Box 2 with the microscope in Box 0
box_2[0], box_0[1] = box_0[1], box_2[0]

# Put the bracelet and blender into Box 3
box_3.extend(['bracelet', 'blender'])

# Empty Box 3
box_3.clear()

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)