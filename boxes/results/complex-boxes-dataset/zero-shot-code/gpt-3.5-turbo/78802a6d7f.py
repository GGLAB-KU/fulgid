box_0 = ['lamp', 'clock', 'tiger', 'headphone']
box_1 = ['brush']
box_2 = ['button']
box_3 = []
box_4 = ['bell', 'zipper', 'toothpaste', 'microwave']
box_5 = ['lightning']

# Swap brush in Box 1 with zipper in Box 4
box_1[0], box_4[1] = box_4[1], box_1[0]

# Move tiger, headphone, and clock from Box 0 to Box 4
box_4.extend(box_0[2:])
box_0 = []

# Remove button from Box 2
box_2 = []

# Move zipper from Box 1 to Box 0
box_0.append(box_1.pop(0))

# Replace lightning with frame in Box 5
box_5[0] = 'frame'

# Put controller, razor, and sculpture into Box 3
box_3.extend(['controller', 'razor', 'sculpture'])

# Swap zipper in Box 0 with brush in Box 4
box_0[0], box_4[1] = box_4[1], box_0[0]

# Move tiger and bell from Box 4 to Box 5
box_5.extend(box_4[2:])
box_4 = box_4[:2]

# Print the contents of each box
print("Box 0:", box_0)
print("Box 1:", box_1)
print("Box 2:", box_2)
print("Box 3:", box_3)
print("Box 4:", box_4)
print("Box 5:", box_5)