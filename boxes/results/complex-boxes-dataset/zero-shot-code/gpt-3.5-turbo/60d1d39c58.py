box0 = ['train', 'lamp']
box1 = ['cow', 'pan']
box2 = ['bracelet']
box3 = ['moon', 'elephant']
box4 = ['spoon', 'wallet', 'fish']

# Swap train and fish
box0[0], box4[2] = box4[2], box0[0]

# Move lamp and fish to box2
box2.extend([box0.pop(1), box0.pop(1)])

# Put wig, pants, and plate into box3
box3.extend(['wig', 'pants', 'plate'])

# Put rain and cloud into box4
box4.extend(['rain', 'cloud'])

# Move bracelet, lamp, and fish to box4
box4.extend([box2.pop(0), box2.pop(0), box2.pop(0)])

# Swap pan and moon
box1[1], box3[0] = box3[0], box1[1]

# Move moon and cow to box2
box2.extend([box1.pop(0), box1.pop(0)])

# Replace wallet and train with battery and branch
box4[1] = 'battery'
box4[0] = 'branch'

# Print the contents of each box
print("Box 0:", box0)
print("Box 1:", box1)
print("Box 2:", box2)
print("Box 3:", box3)
print("Box 4:", box4)