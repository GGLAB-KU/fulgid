box_0 = ['card']
box_1 = ['plate', 'toothpaste', 'laptop']
box_2 = ['cloud']
box_3 = ['beach', 'zipper']
box_4 = ['rocket', 'speaker', 'wig']
box_5 = ['bracelet']
box_6 = ['island', 'truck']

# Swap the rocket in Box 4 with the card in Box 0
box_0[0], box_4[0] = box_4[0], box_0[0]

# Swap the wig in Box 4 with the rocket in Box 0
box_0[0], box_4[2] = box_4[2], box_0[0]

# Swap the bracelet in Box 5 with the rocket in Box 4
box_4[0], box_5[0] = box_5[0], box_4[0]

# Put the pot and the card into Box 0
box_0.extend(['pot', 'card'])

# Put the pants into Box 3
box_3.append('pants')

# Move the bracelet and the speaker from Box 4 to Box 3
box_3.extend([box_4.pop(0), box_4.pop(1)])

# Remove the pot and the wig and the card from Box 0
box_0 = []

# Replace the rocket with the rain in Box 5
box_5[0] = 'rain'

# Replace the rain with the cat in Box 5
box_5[0] = 'cat'

# Replace the truck and the island with the perfume and the dress in Box 6
box_6 = ['perfume', 'dress']

# Remove the cat from Box 5
box_5 = []

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)