box_0 = ['laptop', 'desert', 'lion']
box_1 = ['cow', 'fork', 'tape', 'bracelet']
box_2 = []
box_3 = ['zipper', 'microwave', 'wire']
box_4 = ['makeup', 'thunder', 'grinder']
box_5 = []
box_6 = ['piano', 'headphone']
box_7 = ['pot', 'river', 'fish', 'doll', 'phone']
box_8 = ['glasses', 'shoes', 'grass']

# Put the charger and the blender and the grinder into Box 0
box_0.extend(['charger', 'blender', 'grinder'])

# Swap the fish in Box 7 with the lion in Box 0
box_0.remove('lion')
box_7.remove('fish')
box_0.append('fish')
box_7.append('lion')

# Swap the blender in Box 0 with the grass in Box 8
box_0.remove('blender')
box_8.remove('grass')
box_0.append('grass')
box_8.append('blender')

# Move the grinder and the thunder from Box 4 to Box 7
box_4.remove('grinder')
box_4.remove('thunder')
box_7.extend(['grinder', 'thunder'])

# Put the rocket and the train into Box 3
box_3.extend(['rocket', 'train'])

# Swap the rocket in Box 3 with the headphone in Box 6
box_3.remove('rocket')
box_6.remove('headphone')
box_3.append('headphone')
box_6.append('rocket')

# Replace the desert and the fish and the grinder with the octopus and the submarine and the note in Box 0
box_0.remove('desert')
box_0.remove('fish')
box_0.remove('grinder')
box_0.extend(['octopus', 'submarine', 'note'])

# Put the scissors into Box 4
box_4.append('scissors')

# Remove the thunder from Box 7
box_7.remove('thunder')

# Put the polish and the blanket and the plane into Box 4
box_4.extend(['polish', 'blanket', 'plane'])

# Put the bowl and the forest into Box 0
box_0.extend(['bowl', 'forest'])

# Remove the grinder from Box 7
box_7.remove('grinder')

# Remove the lion and the phone from Box 7
box_7.remove('lion')
box_7.remove('phone')

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