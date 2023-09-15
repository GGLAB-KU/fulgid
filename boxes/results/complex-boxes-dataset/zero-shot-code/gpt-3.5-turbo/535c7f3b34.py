box_0 = ['cup', 'train', 'shorts']
box_1 = ['puzzle', 'headphone', 'bicycle', 'mirror', 'piano']
box_2 = ['phone', 'rock', 'sun', 'chair']
box_3 = ['plane']
box_4 = []
box_5 = []
box_6 = ['leaf', 'toy', 'brush']
box_7 = ['beach', 'storm', 'clock', 'toothbrush', 'sculpture']
box_8 = ['butterfly', 'telescope', 'truck']
box_9 = []

# Replace the items in Box 8
box_8 = ['horn', 'dolphin', 'toothpaste']

# Put the items in Box 0
box_0 = ['cup', 'sun', 'tape']

# Put the items in Box 4
box_4 = ['toothbrush', 'belt']

# Put the items in Box 5
box_5 = ['apple', 'battery', 'ship']

# Replace the items in Box 2
box_2 = ['lightning', 'shoes']

# Remove the shoes from Box 2
box_2.remove('shoes')

# Replace the storm with the boot in Box 7
box_7[1] = 'boot'

# Move the items from Box 5 to Box 6
box_6.extend(box_5)
box_5 = []

# Remove the items from Box 2
box_2 = []

# Swap the sculpture in Box 7 with the toothbrush in Box 4
box_7[4], box_4[1] = box_4[1], box_7[4]

# Remove the items from Box 6
box_6 = []

# Replace the apple with the cow in Box 5
box_5 = ['cow']

# Remove the dolphin from Box 8
box_8.remove('dolphin')

# Swap the train in Box 0 with the toothpaste in Box 8
box_0[1], box_8[2] = box_8[2], box_0[1]

# Replace the plane with the razor in Box 3
box_3[0] = 'razor'

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