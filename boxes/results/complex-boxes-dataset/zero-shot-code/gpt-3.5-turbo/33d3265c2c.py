box0 = ['rock', 'comet', 'forest']
box1 = []
box2 = []
box3 = ['tree']
box4 = ['zipper', 'pillow']

# Replace the tree with the ocean in Box 3
box3.remove('tree')
box3.append('ocean')

# Swap the forest in Box 0 with the ocean in Box 3
box0.remove('forest')
box0.append('ocean')

# Empty Box 3
box3 = []

# Move the pillow and the zipper from Box 4 to Box 0
box0.extend(box4)
box4 = []

# Replace the comet and the rock and the ocean with the glove and the lamp and the bear in Box 0
box0 = ['glove', 'lamp', 'bear']

# Move the bear and the lamp and the zipper from Box 0 to Box 3
box3.extend(box0[1:])
box0 = box0[:1]

# Swap the bear in Box 3 with the glove in Box 0
box0[0], box3[1] = box3[1], box0[0]

# Remove the bear and the pillow from Box 0
box0.remove('bear')
box0.remove('pillow')

# Print the final state of the boxes
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)