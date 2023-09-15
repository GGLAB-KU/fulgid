box_0 = []
box_1 = []
box_2 = ['bird', 'toothbrush', 'car', 'seaweed', 'rain']
box_3 = ['shampoo', 'puzzle', 'train', 'plane', 'freezer']
box_4 = ['piano', 'toothpaste', 'storm']
box_5 = ['cloud']
box_6 = []
box_7 = ['sculpture', 'fish', 'grass']
box_8 = ['keyboard']

# Swap sculpture with keyboard
box_7.remove('sculpture')
box_7.append('keyboard')
box_8.remove('keyboard')
box_8.append('sculpture')

# Move keyboard from box 7 to box 0
box_7.remove('keyboard')
box_0.append('keyboard')

# Empty box 8
box_8 = []

# Put puzzle into box 8
box_8.append('puzzle')

# Remove keyboard from box 0
box_0.remove('keyboard')

# Move toothbrush from box 2 to box 3
box_2.remove('toothbrush')
box_3.append('toothbrush')

# Remove puzzle from box 8
box_8.remove('puzzle')

# Move cloud from box 5 to box 1
box_5.remove('cloud')
box_1.append('cloud')

# Move cloud from box 1 to box 2
box_1.remove('cloud')
box_2.append('cloud')

# Put meteor and oven into box 4
box_4.extend(['meteor', 'oven'])

# Swap puzzle in box 3 with fish in box 7
box_3.remove('puzzle')
box_3.append('fish')
box_7.remove('fish')
box_7.append('puzzle')

# Replace storm, oven, and piano with shirt, boat, and pan in box 4
box_4 = ['shirt', 'boat', 'pan']

# Remove puzzle and grass from box 7
box_7.remove('puzzle')
box_7.remove('grass')

# Swap bird in box 2 with shampoo in box 3
box_2.remove('bird')
box_2.append('shampoo')
box_3.remove('shampoo')
box_3.append('bird')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)