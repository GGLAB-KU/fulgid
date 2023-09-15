box0 = ['watch', 'comb', 'river']
box1 = ['cloud', 'soap']
box2 = ['train', 'toaster', 'glove', 'microwave', 'desert']
box3 = ['cup', 'shark', 'butterfly', 'microscope', 'grinder']
box4 = []
box5 = ['whistle', 'shelf', 'submarine', 'pan', 'grass']

# Put the earring and the harmonica and the tie into Box 4
box4.extend(['earring', 'harmonica', 'tie'])

# Replace the cup and the shark and the grinder with the bird and the keyboard and the octopus in Box 3
box3[0:3] = ['bird', 'keyboard', 'octopus']

# Swap the microwave in Box 2 with the butterfly in Box 3
box2[3], box3[2] = box3[2], box2[3]

# Move the soap and the cloud from Box 1 to Box 4
box4.extend(box1)
box1.clear()

# Swap the river in Box 0 with the grass in Box 5
box0[2], box5[4] = box5[4], box0[2]

# Remove the octopus from Box 3
box3.remove('octopus')

# Remove the watch and the comb from Box 0
box0.remove('watch')
box0.remove('comb')

# Swap the river in Box 5 with the glove in Box 2
box5[4], box2[2] = box2[2], box5[4]

# Remove the grass from Box 0
box0.remove('grass')

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)
print("Box 5:", box5)