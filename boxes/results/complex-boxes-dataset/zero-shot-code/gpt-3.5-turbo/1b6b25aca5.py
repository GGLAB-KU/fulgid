box_0 = ['fridge', 'spoon', 'ocean', 'freezer']
box_1 = ['blender', 'snow', 'game', 'dress']
box_2 = ['card', 'sculpture', 'laptop']
box_3 = ['wire', 'note', 'bicycle']

# Put the chair and the tie into Box 0
box_0.extend(['chair', 'tie'])

# Move the dress and the blender and the snow from Box 1 to Box 0
box_0.extend(box_1[1:4])

# Remove the dress and the ocean and the snow from Box 0
box_0.remove('dress')
box_0.remove('ocean')
box_0.remove('snow')

# Swap the game in Box 1 with the note in Box 3
box_1[2], box_3[1] = box_3[1], box_1[2]

# Swap the wire in Box 3 with the freezer in Box 0
box_3[0], box_0[3] = box_0[3], box_3[0]

# Put the plate and the chair and the battery into Box 3
box_3.extend(['plate', 'chair', 'battery'])

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)