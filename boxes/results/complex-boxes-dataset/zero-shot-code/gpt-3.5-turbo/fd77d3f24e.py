box_0 = ['lipstick']
box_1 = ['jacket', 'wire', 'plate', 'grinder']
box_2 = ['earring', 'island', 'pillow', 'mixer', 'oven']
box_3 = ['blender', 'button', 'mountain', 'whistle', 'rock']
box_4 = ['makeup', 'violin', 'lamp', 'rain', 'pot']
box_5 = ['piano']
box_6 = ['dolphin', 'scissors', 'camera', 'magnet']

# Swap the jacket in Box 1 with the blender in Box 3
box_1.remove('jacket')
box_3.remove('blender')
box_1.append('blender')
box_3.append('jacket')

# Put the jacket into Box 4
box_1.remove('jacket')
box_4.append('jacket')

# Move the mountain and the jacket from Box 3 to Box 1
box_3.remove('mountain')
box_1.append('mountain')

# Swap the piano in Box 5 with the makeup in Box 4
box_5.remove('piano')
box_4.remove('makeup')
box_5.append('makeup')
box_4.append('piano')

# Replace the lipstick with the table in Box 0
box_0.remove('lipstick')
box_0.append('table')

# Move the makeup from Box 5 to Box 4
box_5.remove('makeup')
box_4.append('makeup')

# Put the comb into Box 4
box_4.append('comb')

# Put the jungle into Box 1
box_1.append('jungle')

# Move the rain and the comb and the lamp from Box 4 to Box 3
box_4.remove('rain')
box_4.remove('comb')
box_4.remove('lamp')
box_3.append('rain')
box_3.append('comb')
box_3.append('lamp')

# Swap the jacket in Box 4 with the jacket in Box 1
box_4.remove('jacket')
box_1.remove('jacket')
box_4.append('jacket')
box_1.append('jacket')

# Put the truck and the shampoo into Box 5
box_5.append('truck')
box_5.append('shampoo')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)