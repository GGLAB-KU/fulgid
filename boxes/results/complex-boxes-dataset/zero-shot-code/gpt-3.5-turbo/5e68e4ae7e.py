box_0 = []
box_1 = ['star', 'toothpaste', 'speaker']
box_2 = ['mirror']
box_3 = ['toy', 'sock', 'swimsuit', 'ring', 'rocket']
box_4 = ['scissors', 'tie', 'grinder', 'car', 'island']
box_5 = ['tree', 'boot']
box_6 = ['blanket', 'lion', 'horse']
box_7 = ['horn', 'soap']
box_8 = ['shorts', 'telescope']

# Replace the boot and the tree with the battery and the bag in Box 5
box_5 = ['battery', 'bag']

# Replace the tie and the island with the car and the phone in Box 4
box_4 = ['car', 'phone']

# Move the sock from Box 3 to Box 0
box_0.append(box_3.pop(box_3.index('sock')))

# Replace the mirror with the oven in Box 2
box_2 = ['oven']

# Replace the rocket and the toy with the magnet and the shelf in Box 3
box_3 = ['magnet', 'shelf']

# Move the soap from Box 7 to Box 6
box_6.append(box_7.pop(box_7.index('soap')))

# Put the cat and the sun and the river into Box 4
box_4.extend(['cat', 'sun', 'river'])

# Swap the speaker in Box 1 with the bag in Box 5
box_1, box_5 = box_5, box_1

# Swap the oven in Box 2 with the grinder in Box 4
box_2, box_4 = box_4, box_2

# Swap the bag in Box 1 with the shorts in Box 8
box_1, box_8 = box_8, box_1

# Swap the ring in Box 3 with the shorts in Box 1
box_3[box_3.index('ring')], box_1[box_1.index('shorts')] = box_1[box_1.index('shorts')], box_3[box_3.index('ring')]

# Swap the shorts in Box 3 with the horn in Box 7
box_3[box_3.index('shorts')], box_7[box_7.index('horn')] = box_7[box_7.index('horn')], box_3[box_3.index('shorts')]

# Move the speaker from Box 5 to Box 0
box_0.append(box_5.pop(box_5.index('speaker')))

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)
print("Box 8:", box_8)