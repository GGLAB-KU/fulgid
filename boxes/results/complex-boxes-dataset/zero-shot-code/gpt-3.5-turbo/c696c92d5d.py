box_0 = ['towel', 'piano', 'leaf', 'ship']
box_1 = ['lion']
box_2 = ['dog', 'jacket', 'shoes', 'pillow']
box_3 = ['clock']
box_4 = ['freezer']
box_5 = ['toy']
box_6 = ['scarf']
box_7 = ['table', 'submarine', 'octopus', 'whistle', 'shirt']
box_8 = ['key', 'lamp', 'helmet']

# Swap the clock in Box 3 with the lion in Box 1
box_3, box_1 = box_1, box_3

# Replace the lion with the tie in Box 3
box_3 = ['tie']

# Replace the scarf with the bowl in Box 6
box_6 = ['bowl']

# Put the game into Box 0
box_0.append('game')

# Move the dog and the pillow and the shoes from Box 2 to Box 4
box_4.extend(box_2.pop(0))
box_4.extend(box_2.pop(0))
box_4.extend(box_2.pop(0))

# Move the towel from Box 0 to Box 8
box_8.append(box_0.pop(0))

# Swap the jacket in Box 2 with the dog in Box 4
box_2[0], box_4[0] = box_4[0], box_2[0]

# Move the dog from Box 2 to Box 6
box_6.append(box_2.pop(0))

# Put the makeup into Box 8
box_8.append('makeup')

# Move the toy from Box 5 to Box 6
box_6.append(box_5.pop(0))

# Swap the clock in Box 1 with the leaf in Box 0
box_1[0], box_0[2] = box_0[2], box_1[0]

# Move the game from Box 0 to Box 6
box_6.append(box_0.pop(0))

# Put the tie and the frame into Box 0
box_0.extend(['tie', 'frame'])

# Put the river into Box 7
box_7.append('river')

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