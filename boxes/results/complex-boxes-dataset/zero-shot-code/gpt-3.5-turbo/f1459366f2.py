box_0 = ['dress', 'truck', 'sock', 'leaf']
box_1 = ['sun']
box_2 = ['elephant']
box_3 = []
box_4 = ['scissors', 'shoe', 'train', 'thread', 'pan']
box_5 = []
box_6 = ['table', 'soap', 'seaweed']
box_7 = []
box_8 = []

# Swap the sock in Box 0 with the table in Box 6
box_0[2], box_6[0] = box_6[0], box_0[2]

# Replace the elephant with the shirt in Box 2
box_2[0] = 'shirt'

# Empty Box 4
box_4 = []

# Put the meteor and the pen and the shoes into Box 5
box_5.extend(['meteor', 'pen', 'shoes'])

# Move the soap from Box 6 to Box 5
box_5.append(box_6.pop(1))

# Swap the shirt in Box 2 with the table in Box 0
box_0[0], box_2[0] = box_2[0], box_0[0]

# Move the table from Box 2 to Box 5
box_5.append(box_2.pop(0))

# Replace the shoes and the meteor with the blanket and the boat in Box 5
box_5.remove('shoes')
box_5.remove('meteor')
box_5.extend(['blanket', 'boat'])

# Move the boat from Box 5 to Box 7
box_7.append(box_5.pop(4))

# Put the island into Box 8
box_8.append('island')

# Move the shirt and the leaf from Box 0 to Box 5
box_5.extend([box_0.pop(0), box_0.pop(2)])

# Put the beach into Box 8
box_8.append('beach')

# Empty Box 7
box_7 = []

# Remove the soap and the table and the shirt from Box 5
box_5.remove('soap')
box_5.remove('table')
box_5.remove('shirt')

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