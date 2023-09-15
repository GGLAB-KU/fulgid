box_0 = ['earring']
box_1 = ['polish', 'tie', 'fridge', 'car', 'starfish']
box_2 = ['table']
box_3 = ['telescope', 'drum', 'spoon', 'planet']
box_4 = ['forest', 'storm', 'helmet', 'guitar', 'cup']

# Remove items from Box 1
box_1.remove('starfish')
box_1.remove('fridge')
box_1.remove('polish')

# Move table from Box 2 to Box 1
box_1.append('table')
box_2.remove('table')

# Remove storm from Box 4
box_4.remove('storm')

# Put bowl into Box 3
box_3.append('bowl')

# Swap earring in Box 0 with spoon in Box 3
box_0[0], box_3[2] = box_3[2], box_0[0]

# Remove spoon from Box 0
box_0.remove('spoon')

# Remove car, tie, and table from Box 1
box_1.remove('car')
box_1.remove('tie')
box_1.remove('table')

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)