box_0 = ['ocean', 'harmonica']
box_1 = ['note']
box_2 = ['desert']
box_3 = []
box_4 = ['planet', 'flower', 'shorts', 'horse']
box_5 = ['polish', 'fish', 'motorcycle']
box_6 = ['crown', 'thunder', 'tree', 'blanket', 'bag']

# Remove the desert from Box 2
box_2.remove('desert')

# Swap the fish in Box 5 with the note in Box 1
box_1[0], box_5[1] = box_5[1], box_1[0]

# Move the fish from Box 1 to Box 3
box_3.append(box_1.pop())

# Replace the fish with the pan in Box 3
box_3[0] = 'pan'

# Remove the crown and the tree from Box 6
box_6.remove('crown')
box_6.remove('tree')

# Remove the harmonica and the ocean from Box 0
box_0.remove('harmonica')
box_0.remove('ocean')

# Empty Box 4
box_4.clear()

# Put the hat into Box 0
box_0.append('hat')

# Swap the note in Box 5 with the bag in Box 6
box_5[0], box_6[4] = box_6[4], box_5[0]

# Swap the polish in Box 5 with the hat in Box 0
box_5[0], box_0[0] = box_0[0], box_5[0]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)