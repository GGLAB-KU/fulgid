box_0 = ['chair', 'shoes']
box_1 = []
box_2 = ['makeup', 'needle']
box_3 = ['crown', 'planet', 'tree', 'star']
box_4 = ['grass', 'book', 'starfish', 'sun']

# Replace the skirt with the shoes in Box 0
box_0.remove('shoes')
box_0.append('skirt')

# Remove the needle and the makeup from Box 2
box_2.remove('makeup')
box_2.remove('needle')

# Swap the shoes in Box 0 with the tree in Box 3
box_0.remove('skirt')
box_3.remove('tree')
box_0.append('tree')
box_3.append('skirt')

# Put the shirt into Box 3
box_3.append('shirt')

# Remove the sculpture from Box 2
box_2.remove('sculpture')

# Replace the crown with the frame in Box 3
box_3.remove('crown')
box_3.append('frame')

# Remove the star and the planet and the frame from Box 3
box_3.remove('star')
box_3.remove('planet')
box_3.remove('frame')

# Remove the book and the grass from Box 4
box_4.remove('book')
box_4.remove('grass')

# Print the final contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)