box_0 = ['seaweed', 'motorcycle', 'sun', 'forest', 'glove']
box_1 = ['needle']
box_2 = ['dice', 'magnet', 'headphone', 'shelf']
box_3 = ['pants', 'shirt', 'lamp']
box_4 = []
box_5 = ['grass', 'mirror', 'submarine', 'perfume', 'branch']
box_6 = []
box_7 = []
box_8 = ['moon', 'swimsuit', 'sandals']
box_9 = []

# Swap the sandals in Box 8 with the shirt in Box 3
box_8[2], box_3[1] = box_3[1], box_8[2]

# Put the apple and the chair and the thread into Box 9
box_9.extend(['apple', 'chair', 'thread'])

# Put the dice into Box 8
box_8.append(box_2.pop(0))

# Move the thread from Box 9 to Box 6
box_6.append(box_9.pop(2))

# Move the grass and the perfume from Box 5 to Box 0
box_0.extend([box_5.pop(0), box_5.pop(1)])

# Empty Box 9
box_9.clear()

# Replace the perfume and the seaweed and the forest with the flute and the butterfly and the soap in Box 0
box_0[0] = 'flute'
box_0[3] = 'butterfly'
box_0[4] = 'soap'

# Swap the sandals in Box 3 with the thread in Box 6
box_3[2], box_6[0] = box_6[0], box_3[2]

# Replace the branch with the forest in Box 5
box_5[3] = 'forest'

# Replace the submarine and the mirror and the forest with the camera and the table and the dress in Box 5
box_5[2] = 'camera'
box_5[3] = 'table'
box_5.append('dress')

# Remove the needle from Box 1
box_1.clear()

# Put the dice and the boat into Box 2
box_2.extend(['dice', 'boat'])

# Swap the table in Box 5 with the shirt in Box 8
box_5[3], box_8[1] = box_8[1], box_5[3]

# Move the headphone and the boat and the rain from Box 2 to Box 0
box_0.extend([box_2.pop(2), box_2.pop(1), 'rain'])

# Put the leaf and the battery into Box 8
box_8.extend(['leaf', 'battery'])

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