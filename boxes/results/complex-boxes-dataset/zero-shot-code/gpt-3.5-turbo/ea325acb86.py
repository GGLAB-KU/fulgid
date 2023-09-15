box_0 = []
box_1 = ['plane', 'gloves', 'laptop']
box_2 = ['bus', 'oven', 'microwave']
box_3 = ['mixer', 'bracelet', 'razor', 'bowl', 'sculpture']
box_4 = ['telescope', 'shark', 'scissors', 'bell', 'bird']
box_5 = ['flower', 'motorcycle', 'vase', 'branch', 'speaker']
box_6 = []
box_7 = []

# Swap telescope in Box 4 with bus in Box 2
box_4[0], box_2[0] = box_2[0], box_4[0]

# Move scissors from Box 4 to Box 3
scissors = box_4.pop(2)
box_3.append(scissors)

# Replace scissors, bracelet, and sculpture with mask, toothpaste, and tape in Box 3
box_3[2:5] = ['mask', 'toothpaste', 'tape']

# Move mask from Box 3 to Box 5
mask = box_3.pop(2)
box_5.append(mask)

# Remove shark and bell from Box 4
box_4.remove('shark')
box_4.remove('bell')

# Move bird and bus from Box 4 to Box 5
bird = box_4.pop(2)
bus = box_4.pop(1)
box_5.extend([bird, bus])

# Swap telescope in Box 2 with bus in Box 5
box_2[0], box_5[1] = box_5[1], box_2[0]

# Put bear and shirt into Box 4
box_4.extend(['bear', 'shirt'])

# Replace oven with boat in Box 2
box_2[1] = 'boat'

# Put violin into Box 3
box_3.append('violin')

# Remove shirt and bear from Box 4
box_4.remove('shirt')
box_4.remove('bear')

# Swap gloves in Box 1 with razor in Box 3
box_1[1], box_3[1] = box_3[1], box_1[1]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)
print("Box 6:", box_6)
print("Box 7:", box_7)