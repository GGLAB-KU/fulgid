box_0 = ['mask', 'scissors', 'thread', 'toaster']
box_1 = []
box_2 = ['wig']
box_3 = ['rocket', 'flower']
box_4 = ['shoe']
box_5 = ['sun', 'cow', 'piano', 'elephant', 'note']
box_6 = []
box_7 = ['console', 'tiger', 'cat']
box_8 = ['bicycle', 'necklace', 'storm', 'clock', 'plate']
box_9 = ['zipper', 'blanket', 'pen', 'shirt', 'puzzle']
box_10 = ['towel', 'crown', 'mountain', 'shorts', 'cup']

# Replace the shorts with the paint in Box 10
box_10[3] = 'paint'

# Empty Box 5
box_5 = []

# Swap the cup in Box 10 with the cat in Box 7
box_10[4], box_7[2] = box_7[2], box_10[4]

# Swap the tiger in Box 7 with the bicycle in Box 8
box_7[1], box_8[0] = box_8[0], box_7[1]

# Move the plate and the necklace from Box 8 to Box 7
box_7.extend(box_8[2:4])
box_8 = box_8[:2] + box_8[4:]

# Put the river and the glasses and the sculpture into Box 1
box_1.extend(['river', 'glasses', 'sculpture'])

# Remove the shoe from Box 4
box_4 = []

# Move the mountain and the cat from Box 10 to Box 6
box_6.extend([box_10[2], box_7[2]])
box_10[2] = box_7[2] = []

# Remove the necklace and the bicycle from Box 7
box_7 = box_7[:1] + box_7[3:]

# Swap the paint in Box 10 with the plate in Box 7
box_10[3], box_7[2] = box_7[2], box_10[3]

# Remove the cat from Box 6
box_6[1] = []

# Remove the wig from Box 2
box_2 = []

# Remove the plate from Box 10
box_10[3] = []

# Move the storm and the tiger from Box 8 to Box 0
box_0.extend(box_8[2:4])
box_8 = box_8[:2] + box_8[4:]

# Remove the toaster and the mask from Box 0
box_0 = box_0[2:]

# Remove the cup and the console and the paint from Box 7
box_7 = box_7[:1]

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