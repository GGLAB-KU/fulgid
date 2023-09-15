box_0 = ['scissors', 'shark']
box_1 = ['wire']
box_2 = []
box_3 = []
box_4 = ['train']
box_5 = ['gloves', 'shelf', 'tree', 'paint']
box_6 = ['oven']

# Swap the oven in Box 6 with the train in Box 4
box_4, box_6 = box_6, box_4

# Swap the wire in Box 1 with the shark in Box 0
box_0[0], box_1[0] = box_1[0], box_0[0]

# Put the shoes and the tree and the camera into Box 1
box_1.extend(['shoes', 'tree', 'camera'])

# Empty Box 6
box_6 = []

# Put the mountain into Box 0
box_0.append('mountain')

# Swap the paint in Box 5 with the oven in Box 4
box_4[0], box_5[3] = box_5[3], box_4[0]

# Remove the oven and the shelf from Box 5
box_5.remove('oven')
box_5.remove('shelf')

# Replace the mountain and the wire with the pillow and the ocean in Box 0
box_0 = ['pillow', 'ocean']

# Remove the tree and the gloves from Box 5
box_5.remove('tree')
box_5.remove('gloves')

# Remove the paint from Box 4
box_4 = []

# Empty Box 0
box_0 = []

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)