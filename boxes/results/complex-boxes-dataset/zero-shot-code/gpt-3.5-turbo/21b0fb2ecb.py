box_0 = []
box_1 = ['pan', 'wire', 'shoe', 'perfume']
box_2 = []
box_3 = ['starfish', 'microwave']
box_4 = ['cloud', 'blanket']
box_5 = []
box_6 = []

# Put the pants, swimsuit, and thunder into Box 3
box_3.extend(['pants', 'swimsuit', 'thunder'])

# Replace the microwave with the rock in Box 3
box_3.remove('microwave')
box_3.append('rock')

# Put the mountain, octopus, and violin into Box 2
box_2.extend(['mountain', 'octopus', 'violin'])

# Swap the swimsuit in Box 3 with the octopus in Box 2
box_3.remove('swimsuit')
box_2.remove('octopus')
box_3.append('octopus')
box_2.append('swimsuit')

# Put the magnet and toaster into Box 4
box_4.extend(['magnet', 'toaster'])

# Remove the swimsuit and mountain from Box 2
box_2.remove('swimsuit')
box_2.remove('mountain')

# Swap the violin in Box 2 with the starfish in Box 3
box_2.append('starfish')
box_3.remove('starfish')
box_3.append('violin')

# Put the belt and bag into Box 6
box_6.extend(['belt', 'bag'])

# Move the cloud, magnet, and blanket from Box 4 to Box 0
box_0.extend(['cloud', 'magnet', 'blanket'])
box_4.remove('cloud')
box_4.remove('magnet')
box_4.remove('blanket')

# Replace the wire and perfume with the shampoo and cow in Box 1
box_1.remove('wire')
box_1.remove('perfume')
box_1.extend(['shampoo', 'cow'])

# Remove the belt and bag from Box 6
box_6.remove('belt')
box_6.remove('bag')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)