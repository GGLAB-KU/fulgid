box_0 = ['helmet', 'elephant', 'skirt']
box_1 = ['laptop', 'perfume', 'leaf']
box_2 = ['storm', 'bicycle', 'hat', 'earring']
box_3 = ['star']
box_4 = []
box_5 = []
box_6 = ['lamp']

# Swap the lamp in Box 6 with the leaf in Box 1
box_6[0], box_1[2] = box_1[2], box_6[0]

# Swap the leaf in Box 6 with the perfume in Box 1
box_6[0], box_1[1] = box_1[1], box_6[0]

# Move the perfume from Box 6 to Box 2
box_2.append(box_6.pop(0))

# Swap the lamp in Box 1 with the skirt in Box 0
box_1[0], box_0[2] = box_0[2], box_1[0]

# Put the blanket and the plane and the forest into Box 3
box_3.extend(['blanket', 'plane', 'forest'])

# Put the flute and the mask and the card into Box 6
box_6.extend(['flute', 'mask', 'card'])

# Move the flute and the card from Box 6 to Box 1
box_1.extend(box_6[1:3])
box_6 = box_6[:1] + box_6[3:]

# Put the river into Box 4
box_4.append('river')

# Swap the lamp in Box 0 with the perfume in Box 2
box_0[0], box_2[1] = box_2[1], box_0[0]

# Swap the earring in Box 2 with the plane in Box 3
box_2[3], box_3[1] = box_3[1], box_2[3]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)