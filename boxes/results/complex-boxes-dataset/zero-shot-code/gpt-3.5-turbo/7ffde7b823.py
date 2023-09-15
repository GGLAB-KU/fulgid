box_0 = ['console', 'lion', 'pillow', 'rain', 'umbrella']
box_1 = ['blanket', 'ocean', 'dolphin']
box_2 = ['card', 'toothpaste', 'leaf', 'telescope', 'bag']
box_3 = []
box_4 = ['mask', 'tie']

# Remove the mask from Box 4
box_4.remove('mask')

# Swap the tie in Box 4 with the lion in Box 0
box_0.remove('lion')
box_4.append('lion')

# Move the lion from Box 4 to Box 2
box_4.remove('lion')
box_2.append('lion')

# Remove the dolphin and the blanket and the ocean from Box 1
box_1.remove('blanket')
box_1.remove('ocean')
box_1.remove('dolphin')

# Move the rain from Box 0 to Box 1
box_0.remove('rain')
box_1.append('rain')

# Put the puzzle and the hat into Box 4
box_4.append('puzzle')
box_4.append('hat')

# Move the lion from Box 2 to Box 4
box_2.remove('lion')
box_4.append('lion')

# Replace the rain with the perfume in Box 1
box_1.remove('rain')
box_1.append('perfume')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)