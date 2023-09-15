box_0 = []
box_1 = ['dog', 'piano', 'belt', 'toaster', 'violin']
box_2 = ['branch', 'pillow', 'card', 'tiger', 'glasses']
box_3 = ['rock']
box_4 = []
box_5 = ['harmonica', 'blanket', 'scissors', 'forest', 'shark']
box_6 = ['octopus', 'sock']
box_7 = ['toy']

# Remove the forest and the shark from Box 5
box_5.remove('forest')
box_5.remove('shark')

# Move the toy from Box 7 to Box 0
box_0.append(box_7.pop())

# Swap the toy in Box 0 with the octopus in Box 6
box_0[0], box_6[0] = box_6[0], box_0[0]

# Remove the octopus from Box 0
box_0.pop()

# Remove the violin and the piano from Box 1
box_1.remove('violin')
box_1.remove('piano')

# Put the perfume into Box 2
box_2.append('perfume')

# Replace the rock with the octopus in Box 3
box_3[0] = box_6[0]

# Empty Box 3
box_3 = []

# Put the scissors and the umbrella into Box 0
box_0.extend(['scissors', 'umbrella'])

# Swap the toaster in Box 1 with the toy in Box 6
box_1[box_1.index('toaster')], box_6[box_6.index('toy')] = box_6[box_6.index('toy')], box_1[box_1.index('toaster')]

# Remove the belt from Box 1
box_1.remove('belt')

# Empty Box 0
box_0 = []

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)