box_0 = []
box_1 = ['plate', 'drum', 'telescope', 'cow']
box_2 = ['tape', 'blender', 'ocean', 'key']
box_3 = ['lightning']
box_4 = ['sock', 'flower', 'camera', 'river', 'island']
box_5 = ['pants']
box_6 = ['gloves', 'coral', 'table']
box_7 = ['meteor', 'brush', 'charger', 'scissors']
box_8 = ['card', 'mask', 'tiger', 'submarine']

# Put the motorcycle, forest, and shampoo into Box 3
box_3.extend(['motorcycle', 'forest', 'shampoo'])

# Put the glove into Box 2
box_2.append('glove')

# Swap the charger in Box 7 with the submarine in Box 8
box_7.remove('charger')
box_8.remove('submarine')
box_7.append('submarine')
box_8.append('charger')

# Move the shampoo, forest, and motorcycle from Box 3 to Box 2
box_2.extend(box_3[3:])
box_3 = box_3[:3]

# Put the spoon, cow, and charger into Box 2
box_2.extend(['spoon', 'cow', 'charger'])

# Put the apple and button into Box 4
box_4.extend(['apple', 'button'])

# Move the table and gloves from Box 6 to Box 5
box_5.extend(box_6[2:])
box_6 = box_6[:2]

# Put the lock into Box 0
box_0.append('lock')

# Swap the plate in Box 1 with the flower in Box 4
box_1.remove('plate')
box_4.remove('flower')
box_1.append('flower')
box_4.append('plate')

# Move the drum and flower from Box 1 to Box 2
box_2.extend(box_1[1:])
box_1 = box_1[:1]

# Move the meteor, submarine, and scissors from Box 7 to Box 6
box_6.extend(box_7[:3])
box_7 = box_7[3:]

# Put the puzzle and frame into Box 2
box_2.extend(['puzzle', 'frame'])

# Empty Box 0
box_0 = []

# Put the laptop and belt into Box 6
box_6.extend(['laptop', 'belt'])

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