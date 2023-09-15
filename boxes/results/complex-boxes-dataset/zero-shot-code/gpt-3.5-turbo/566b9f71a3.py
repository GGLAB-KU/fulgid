box_0 = ['mountain', 'shark']
box_1 = []
box_2 = ['comb', 'mirror', 'train', 'coral', 'horse']
box_3 = ['blender', 'pen', 'planet', 'tape']
box_4 = ['belt', 'flute']
box_5 = []

# Replace the planet and the blender with the drum and the chair in Box 3
box_3.remove('planet')
box_3.remove('blender')
box_3.append('drum')
box_3.append('chair')

# Replace the horse with the train in Box 2
box_2.remove('horse')
box_2.append('train')

# Swap the belt in Box 4 with the train in Box 2
box_4.remove('belt')
box_2.remove('train')
box_4.append('train')
box_2.append('belt')

# Replace the belt with the glasses in Box 2
box_2.remove('belt')
box_2.append('glasses')

# Move the tape and the pen from Box 3 to Box 5
box_3.remove('tape')
box_3.remove('pen')
box_5.append('tape')
box_5.append('pen')

# Remove the chair from Box 3
box_3.remove('chair')

# Swap the train in Box 4 with the mountain in Box 0
box_4.remove('train')
box_0.remove('mountain')
box_4.append('mountain')
box_0.append('train')

# Put the tree and the moon into Box 5
box_5.append('tree')
box_5.append('moon')

# Put the jacket and the doll and the beach into Box 0
box_0.append('jacket')
box_0.append('doll')
box_0.append('beach')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)