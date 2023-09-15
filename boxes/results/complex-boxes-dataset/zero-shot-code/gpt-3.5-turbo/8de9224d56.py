box_0 = ['necklace', 'mixer', 'toothpaste', 'microscope', 'rain']
box_1 = ['storm', 'sun', 'shorts']
box_2 = ['piano']
box_3 = ['telescope', 'jacket']
box_4 = ['glove', 'bell']
box_5 = ['belt', 'wire', 'apple']
box_6 = []

# Replace the piano with the book in Box 2
box_2.remove('piano')
box_0.append('book')

# Move the glove and the bell from Box 4 to Box 6
box_4.remove('glove')
box_4.remove('bell')
box_6.extend(['glove', 'bell'])

# Move the mixer from Box 0 to Box 1
box_0.remove('mixer')
box_1.append('mixer')

# Remove the apple and the wire and the belt from Box 5
box_5.remove('apple')
box_5.remove('wire')
box_5.remove('belt')

# Put the book into Box 0
box_0.remove('book')
box_0.append('book')

# Move the telescope and the jacket from Box 3 to Box 6
box_3.remove('telescope')
box_3.remove('jacket')
box_6.extend(['telescope', 'jacket'])

# Remove the book from Box 2
box_2.remove('book')

# Replace the toothpaste with the comb in Box 0
box_0.remove('toothpaste')
box_0.append('comb')

# Swap the storm in Box 1 with the bell in Box 6
box_1.remove('storm')
box_6.remove('bell')
box_1.append('bell')
box_6.append('storm')

# Swap the storm in Box 6 with the rain in Box 0
box_6.remove('storm')
box_0.remove('rain')
box_6.append('rain')
box_0.append('storm')

# Replace the sun and the bell with the motorcycle and the plane in Box 1
box_1.remove('sun')
box_1.remove('bell')
box_1.extend(['motorcycle', 'plane'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)