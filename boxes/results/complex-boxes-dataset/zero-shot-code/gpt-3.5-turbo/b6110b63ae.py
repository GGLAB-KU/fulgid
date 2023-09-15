box_0 = ['mountain', 'battery', 'beach']
box_1 = ['whistle', 'thread', 'rock']
box_2 = ['wig']
box_3 = ['tie', 'cup', 'plate', 'microwave']
box_4 = ['butterfly']
box_5 = ['pen', 'rocket', 'phone', 'dice', 'cloud']
box_6 = []
box_7 = ['octopus', 'boat', 'sock', 'snow', 'coat']
box_8 = ['doll', 'shoe', 'mask']

# Swap the butterfly in Box 4 with the wig in Box 2
box_4, box_2 = box_2, box_4

# Replace the pen with the tree in Box 5
box_5[0] = 'tree'

# Swap the octopus in Box 7 with the battery in Box 0
box_7[0], box_0[1] = box_0[1], box_7[0]

# Put the rock into Box 2
box_2.append('rock')

# Remove the rock from Box 2
box_2.remove('rock')

# Replace the tie with the polish in Box 3
box_3[0] = 'polish'

# Swap the boat in Box 7 with the mountain in Box 0
box_7[1], box_0[0] = box_0[0], box_7[1]

# Move the mask and the shoe from Box 8 to Box 7
box_7.extend(box_8[2:])
box_8 = box_8[:2]

# Put the mirror into Box 7
box_7.append('mirror')

# Put the pen into Box 8
box_8.append('pen')

# Put the fridge and the river into Box 5
box_5.extend(['fridge', 'river'])

# Swap the doll in Box 8 with the cup in Box 3
box_8[0], box_3[1] = box_3[1], box_8[0]

# Swap the pen in Box 8 with the boat in Box 0
box_8[2], box_0[1] = box_0[1], box_8[2]

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