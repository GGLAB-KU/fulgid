box_0 = ['forest']
box_1 = ['bird', 'helmet', 'coral', 'glove']
box_2 = ['elephant', 'perfume', 'seaweed']
box_3 = []
box_4 = ['glasses', 'butterfly']
box_5 = ['branch', 'frame', 'sock']
box_6 = ['hat']
box_7 = ['scissors', 'bus']

# Swap scissors in Box 7 with hat in Box 6
box_6, box_7 = box_7, box_6

# Move bird and helmet from Box 1 to Box 5
box_5.extend(box_1[0:2])
box_1 = box_1[2:]

# Put watch, truck, and game into Box 7
box_7.extend(['watch', 'truck', 'game'])

# Move seaweed, elephant, and perfume from Box 2 to Box 5
box_5.extend(box_2[0:3])
box_2 = []

# Remove scissors from Box 6
box_6 = []

# Swap branch in Box 5 with glove in Box 1
box_1[1], box_5[0] = box_5[0], box_1[1]

# Move game, hat, and truck from Box 7 to Box 0
box_0.extend(box_7[2:5])
box_7 = box_7[0:2]

# Remove watch and bus from Box 7
box_7 = box_7[0:1]

# Move forest, game, and truck from Box 0 to Box 7
box_7.extend(box_0[0:3])
box_0 = []

# Swap butterfly in Box 4 with branch in Box 1
box_1[0], box_4[1] = box_4[1], box_1[0]

# Move coral and butterfly from Box 1 to Box 6
box_6.extend(box_1[1:3])
box_1 = box_1[0:1]

# Move helmet and frame from Box 5 to Box 3
box_3.extend(box_5[1:3])
box_5 = box_5[0:1]

print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)