box_0 = ['doll', 'bus', 'scissors', 'ocean', 'fork']
box_1 = ['microwave', 'gloves', 'vase', 'boot']
box_2 = ['blanket', 'jacket', 'perfume']
box_3 = []
box_4 = ['headphone', 'planet']

# Swap the boot in Box 1 with the perfume in Box 2
box_1[3], box_2[2] = box_2[2], box_1[3]

# Move the fork from Box 0 to Box 4
box_4.append(box_0.pop(4))

# Replace the blanket and the boot with the console and the cow in Box 2
box_2[0] = 'console'
box_2[1] = 'cow'

# Remove the jacket and the console from Box 2
box_2.remove('jacket')
box_2.remove('console')

# Remove the cow from Box 2
box_2.remove('cow')

# Remove the scissors and the ocean from Box 0
box_0.remove('scissors')
box_0.remove('ocean')

# Move the microwave from Box 1 to Box 2
box_2.append(box_1.pop(0))

# Print the final contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)