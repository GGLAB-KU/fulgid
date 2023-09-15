box_0 = []
box_1 = ['thunder']
box_2 = ['bracelet', 'needle', 'towel', 'submarine']
box_3 = []
box_4 = ['spoon', 'perfume', 'island', 'truck']
box_5 = ['boat']
box_6 = ['train']
box_7 = ['pen', 'oven', 'bag', 'bicycle']
box_8 = []
box_9 = ['doll', 'storm', 'dice', 'rock']
box_10 = ['crown']

# Swap the thunder in Box 0 with the bicycle in Box 7
box_0, box_7 = box_7, box_0

# Swap the crown in Box 10 with the boat in Box 5
box_10, box_5 = box_5, box_10

# Replace the thunder with the guitar in Box 7
box_7.remove('thunder')
box_7.append('guitar')

# Replace the boat with the dolphin in Box 10
box_10.remove('boat')
box_10.append('dolphin')

# Move the river from Box 1 to Box 0
box_0.append(box_1.pop(0))

# Replace the river with the rocket in Box 0
box_0.remove('river')
box_0.append('rocket')

# Remove the bag and the oven from Box 7
box_7.remove('bag')
box_7.remove('oven')

# Swap the needle in Box 2 with the train in Box 6
box_2.remove('needle')
box_6.remove('train')
box_2.append('train')
box_6.append('needle')

# Remove the rocket and the bicycle from Box 0
box_0.remove('rocket')
box_0.remove('bicycle')

# Put the makeup and the snow into Box 0
box_0.extend(['makeup', 'snow'])

# Empty Box 0
box_0 = []

# Put the shirt into Box 4
box_4.append('shirt')

# Remove the guitar from Box 7
box_7.remove('guitar')

# Replace the shirt and the truck with the grass and the wire in Box 4
box_4.remove('shirt')
box_4.remove('truck')
box_4.extend(['grass', 'wire'])

# Move the bracelet from Box 2 to Box 9
box_2.remove('bracelet')
box_9.append('bracelet')

# Remove the crown from Box 5
box_5.remove('crown')

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
print("Box 9:", box_9)
print("Box 10:", box_10)