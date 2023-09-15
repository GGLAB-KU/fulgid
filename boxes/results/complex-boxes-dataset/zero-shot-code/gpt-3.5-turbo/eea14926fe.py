box_0 = ['lock', 'shark', 'comb', 'note', 'ring']
box_1 = []
box_2 = ['hat']
box_3 = ['fork', 'train', 'puzzle', 'magnet']
box_4 = ['usb', 'whistle']
box_5 = ['rain']
box_6 = ['rock', 'pan']
box_7 = ['plate', 'boat', 'watch', 'grinder']
box_8 = ['shoes', 'soap', 'toothpaste']

# Remove rain from Box 5
box_5.remove('rain')

# Put guitar, mirror, and fork into Box 4
box_4.extend(['guitar', 'mirror', 'fork'])

# Put rock and tape into Box 8
box_8.extend(['rock', 'tape'])

# Move hat from Box 2 to Box 4
box_4.append(box_2.pop(0))

# Replace whistle with octopus in Box 4
box_4.remove('whistle')
box_4.append('octopus')

# Replace shark, note, and comb with blender, doll, and shelf in Box 0
box_0 = ['blender', 'doll', 'shelf']

# Replace doll, blender, and lock with jungle, cow, and camera in Box 0
box_0 = ['jungle', 'cow', 'camera']

# Remove ring from Box 0
box_0.remove('ring')

# Put basket and dice into Box 0
box_0.extend(['basket', 'dice'])

# Remove cow from Box 0
box_0.remove('cow')

# Remove plate and boat from Box 7
box_7.remove('plate')
box_7.remove('boat')

# Empty Box 7
box_7 = []

# Put piano into Box 2
box_2.append('piano')

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